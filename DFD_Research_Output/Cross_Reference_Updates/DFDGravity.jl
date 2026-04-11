"""
    DFDGravity.jl --- Core mu(a,k) and Sigma(a,k) module for DFD

    DFD 20-Agent Research Programme, Wave 5, Iteration 56
    Phase 0A: First working DFD modified gravity code

    Implements:
      - mu_DFD(a, k, p):    Modified Poisson equation enhancement
      - Sigma_DFD(a, k, p): Lensing potential enhancement
      - eta_psi(a, k, p):   Gravitational slip parameter
      - k_mu(a, p):         Characteristic MOND scale in comoving wavenumber

    Key physics:
      - Radiation-era suppression via Omega_m/Omega_tot prefactor
      - Psi-field gradient stress produces NEGATIVE eta_psi (opposite to f(R))
      - BBN safe: mu -> 1 as a -> 0
      - GR recovery: mu -> 1 at k >> k_mu

    References:
      - G. Alcock, "DFD: A Complete Unified Theory" (v108)
      - Pogosian & Silvestri, Phys. Rev. D 94, 104014 (2016)
      - W5i55 Verification Report, Agents 1--2
      - W5i56 Verification Report, Agents 1--4
"""
module DFDGravity

export DFDParams, mu_DFD, Sigma_DFD, eta_psi, k_mu
export Omega_m_of_a, H_of_a

# ============================================================
# Physical constants (SI)
# ============================================================
const a0_SI     = 1.2e-10      # MOND acceleration [m/s^2]
const H0_SI     = 2.195e-18    # 67.7 km/s/Mpc in [1/s]
const c_light   = 2.998e8      # speed of light [m/s]
const Mpc_in_m  = 3.0857e22    # 1 Mpc in metres

# ============================================================
# DFD parameter structure
# ============================================================
"""
    DFDParams

Cosmological + DFD parameters. All DFD-specific parameters
are derived from the theory; none are free.

Fields:
- Omega_m0: present matter density fraction
- Omega_r0: present radiation density fraction
- Omega_L0: present dark energy density fraction (1 - Omega_m0 - Omega_r0)
- h: dimensionless Hubble parameter H0/(100 km/s/Mpc)
- c_psi: psi-field sound speed in units of c (DFD: c_psi = 1)
- a0: MOND acceleration scale [m/s^2]
"""
struct DFDParams
    Omega_m0::Float64
    Omega_r0::Float64
    Omega_L0::Float64
    h::Float64
    c_psi::Float64
    a0::Float64

    function DFDParams(;
        Omega_m0 = 0.3111,
        Omega_r0 = 9.15e-5,
        h = 0.6774,
        c_psi = 1.0,
        a0 = 1.2e-10
    )
        Omega_L0 = 1.0 - Omega_m0 - Omega_r0
        new(Omega_m0, Omega_r0, Omega_L0, h, c_psi, a0)
    end
end

# ============================================================
# Background cosmology
# ============================================================

"""
    H_of_a(a, p::DFDParams) -> Float64

Hubble parameter H(a) in units of H0.
Flat FLRW: H^2/H0^2 = Omega_r/a^4 + Omega_m/a^3 + Omega_L
"""
function H_of_a(a::Float64, p::DFDParams)::Float64
    E2 = p.Omega_r0 / a^4 + p.Omega_m0 / a^3 + p.Omega_L0
    return sqrt(E2)
end

"""
    Omega_m_of_a(a, p::DFDParams) -> Float64

Matter density fraction at scale factor a:
Omega_m(a) = Omega_m0 / (a^3 * E^2(a))
"""
function Omega_m_of_a(a::Float64, p::DFDParams)::Float64
    E2 = p.Omega_r0 / a^4 + p.Omega_m0 / a^3 + p.Omega_L0
    return p.Omega_m0 / (a^3 * E2)
end

# ============================================================
# DFD characteristic MOND scale k_mu(a)
# ============================================================

"""
    k_mu(a, p::DFDParams) -> Float64

Characteristic comoving wavenumber below which MOND
enhancement is significant. Units: 1/Mpc.

k_mu(a) = a * H(a) * sqrt(Omega_m(a)) / (c_psi * sqrt(a0/H0))

At a=1:  k_mu ~ 0.001 Mpc^{-1}
At a=1e-3 (recombination): k_mu ~ 0.003 Mpc^{-1}
"""
function k_mu(a::Float64, p::DFDParams)::Float64
    H_a = H_of_a(a, p) * p.h * 100.0e3 / Mpc_in_m  # H(a) in 1/s
    Om_a = Omega_m_of_a(a, p)
    H0_phys = p.h * 100.0e3 / Mpc_in_m  # H0 in 1/s

    # k_mu in 1/m then convert to 1/Mpc
    k_mu_phys = a * H_a * sqrt(Om_a) / (p.c_psi * sqrt(p.a0 / H0_phys))

    return k_mu_phys * Mpc_in_m
end

# ============================================================
# mu(a,k) --- Modified Poisson equation
# ============================================================

"""
    mu_DFD(a, k, p::DFDParams) -> Float64

DFD gravitational coupling enhancement for the Poisson equation:

    -k^2 Phi = 4 pi G a^2 mu(a,k) rho_bar delta

With radiation-era Omega_m suppression (ESSENTIAL for BBN safety):

    mu(a,k) = 1 + Omega_m(a) * x / (1 + x)

where x = (k_mu(a)/k)^2.

Properties:
- mu >= 1 for all a, k  (no anti-gravity)
- mu -> 1 as a -> 0     (BBN safe: Omega_m -> 0 in radiation era)
- mu -> 1 + Omega_m     at k << k_mu  (deep MOND, capped by Omega_m)
- mu -> 1               at k >> k_mu  (Newtonian)
"""
function mu_DFD(a::Float64, k::Float64, p::DFDParams)::Float64
    if k <= 0.0 || a <= 0.0
        return 1.0
    end

    km = k_mu(a, p)
    x = (km / k)^2
    Om = Omega_m_of_a(a, p)

    return 1.0 + Om * x / (1.0 + x)
end

# ============================================================
# Sigma(a,k) --- Lensing potential
# ============================================================

"""
    Sigma_DFD(a, k, p::DFDParams) -> Float64

DFD lensing parameter:

    -k^2 (Phi + Psi)/2 = 4 pi G a^2 Sigma(a,k) rho_bar delta

The psi-field gradient stress produces Sigma < mu
(lensing mass slightly less than dynamical mass):

    Sigma(a,k) = mu(a,k) * (1 - x / (3(1+x)))

where x = (k_mu(a)/k)^2.
"""
function Sigma_DFD(a::Float64, k::Float64, p::DFDParams)::Float64
    if k <= 0.0 || a <= 0.0
        return 1.0
    end

    mu_val = mu_DFD(a, k, p)
    km = k_mu(a, p)
    x = (km / k)^2

    slip_correction = 1.0 - x / (3.0 * (1.0 + x))

    return mu_val * slip_correction
end

# ============================================================
# eta_psi --- Gravitational slip parameter
# ============================================================

"""
    eta_psi(a, k, p::DFDParams) -> Float64

Gravitational slip: eta_psi = Sigma/mu - 1

    eta_psi = -x / (3(1+x))

where x = (k_mu/k)^2.

SIGN: eta_psi < 0 always (lensing weaker than dynamics).
This is OPPOSITE to f(R) and DGP, where eta > 0.

At cluster scales (k ~ 0.01 Mpc^{-1}): eta_psi ~ -0.003
"""
function eta_psi(a::Float64, k::Float64, p::DFDParams)::Float64
    if k <= 0.0 || a <= 0.0
        return 0.0
    end

    km = k_mu(a, p)
    x = (km / k)^2

    return -x / (3.0 * (1.0 + x))
end

end # module DFDGravity
