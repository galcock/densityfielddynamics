"""
    DFDBackground.jl --- Background cosmology and growth factor for DFD

    DFD 20-Agent Research Programme, Wave 5, Iteration 56
    Phase 0A: Background solver for DFD modified gravity

    Implements:
      - comoving_distance(z, p):       Comoving distance to redshift z
      - growth_factor_DFD(a, k, p):    Scale-dependent growth factor
      - growth_factor_LCDM(a, p):      Standard LCDM growth factor
      - sound_horizon(p):              Sound horizon at drag epoch

    References:
      - Eisenstein & Hu, ApJ 496, 605 (1998)
      - Heath, MNRAS 179, 351 (1977)
      - W5i56 Verification Report, Agent 3
"""
module DFDBackground

# Note: In actual use, this would import from the DFDGravity module.
# For standalone testing, the necessary functions are duplicated here.

export comoving_distance, angular_diameter_distance
export growth_factor_DFD, growth_factor_LCDM
export sound_horizon, DFDParams_BG

# ============================================================
# Physical constants
# ============================================================
const Mpc_in_m  = 3.0857e22

# ============================================================
# Parameter structure (mirrors DFDGravity.DFDParams)
# ============================================================
struct DFDParams_BG
    Omega_m0::Float64
    Omega_r0::Float64
    Omega_L0::Float64
    h::Float64
    c_psi::Float64
    a0::Float64

    function DFDParams_BG(;
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
# Background functions
# ============================================================

function H_of_a(a::Float64, p::DFDParams_BG)::Float64
    E2 = p.Omega_r0 / a^4 + p.Omega_m0 / a^3 + p.Omega_L0
    return sqrt(E2)
end

function Omega_m_of_a(a::Float64, p::DFDParams_BG)::Float64
    E2 = p.Omega_r0 / a^4 + p.Omega_m0 / a^3 + p.Omega_L0
    return p.Omega_m0 / (a^3 * E2)
end

function k_mu_bg(a::Float64, p::DFDParams_BG)::Float64
    H_a = H_of_a(a, p) * p.h * 100.0e3 / Mpc_in_m
    Om_a = Omega_m_of_a(a, p)
    H0_phys = p.h * 100.0e3 / Mpc_in_m
    k_mu_phys = a * H_a * sqrt(Om_a) / (p.c_psi * sqrt(p.a0 / H0_phys))
    return k_mu_phys * Mpc_in_m
end

function mu_DFD_bg(a::Float64, k::Float64, p::DFDParams_BG)::Float64
    if k <= 0.0 || a <= 0.0
        return 1.0
    end
    km = k_mu_bg(a, p)
    x = (km / k)^2
    Om = Omega_m_of_a(a, p)
    return 1.0 + Om * x / (1.0 + x)
end

# ============================================================
# Comoving distance
# ============================================================

"""
    comoving_distance(z, p::DFDParams_BG) -> Float64

Comoving distance to redshift z in Mpc.
chi(z) = c/H0 * integral_0^z dz'/E(z')
Uses Simpson's rule with 1000 points.
"""
function comoving_distance(z::Float64, p::DFDParams_BG)::Float64
    c_over_H0 = 2997.92458 / p.h  # c/H0 in Mpc

    N = 1000
    dz = z / N
    s = 0.0
    for i in 0:N
        zi = i * dz
        ai = 1.0 / (1.0 + zi)
        Ei = H_of_a(ai, p)
        if i == 0 || i == N
            w = 1.0
        elseif iseven(i)
            w = 2.0
        else
            w = 4.0
        end
        s += w / Ei
    end
    return c_over_H0 * s * dz / 3.0
end

"""
    angular_diameter_distance(z, p::DFDParams_BG) -> Float64

Angular diameter distance in Mpc.
d_A = chi(z) / (1+z)
"""
function angular_diameter_distance(z::Float64, p::DFDParams_BG)::Float64
    return comoving_distance(z, p) / (1.0 + z)
end

# ============================================================
# Growth factor
# ============================================================

"""
    growth_factor_DFD(a_final, k, p::DFDParams_BG) -> Float64

Scale-dependent growth factor in DFD.
Solves: D'' + (2 + H'/H) D' - 3/2 Omega_m(a) mu(a,k) D = 0
normalised to D(a_init) = a_init (growing mode in matter era).

Uses 4th-order Runge-Kutta in ln(a).
"""
function growth_factor_DFD(a_final::Float64, k::Float64,
                           p::DFDParams_BG)::Float64
    lna_init = log(1e-4)
    lna_final = log(a_final)

    if lna_final <= lna_init
        return exp(lna_init)
    end

    N = 2000
    dlna = (lna_final - lna_init) / N

    # IC: D = a, dD/dlna = a (growing mode)
    D = exp(lna_init)
    dD = exp(lna_init)

    for i in 1:N
        lna = lna_init + (i - 1) * dlna

        function rhs(lna_loc, D_loc, dD_loc)
            a_loc = exp(lna_loc)
            E = H_of_a(a_loc, p)
            Om = Omega_m_of_a(a_loc, p)
            mu = mu_DFD_bg(a_loc, k, p)

            Om_r = p.Omega_r0 / (a_loc^4 * E^2)
            dlnE = -0.5 * (3.0 * Om + 4.0 * Om_r)

            friction = -(2.0 + dlnE)
            source = 1.5 * Om * mu

            ddD = friction * dD_loc + source * D_loc
            return (dD_loc, ddD)
        end

        # RK4 step
        k1_D, k1_dD = rhs(lna, D, dD)
        k2_D, k2_dD = rhs(lna + 0.5*dlna, D + 0.5*dlna*k1_D,
                           dD + 0.5*dlna*k1_dD)
        k3_D, k3_dD = rhs(lna + 0.5*dlna, D + 0.5*dlna*k2_D,
                           dD + 0.5*dlna*k2_dD)
        k4_D, k4_dD = rhs(lna + dlna, D + dlna*k3_D,
                           dD + dlna*k3_dD)

        D  += dlna * (k1_D  + 2*k2_D  + 2*k3_D  + k4_D)  / 6
        dD += dlna * (k1_dD + 2*k2_dD + 2*k3_dD + k4_dD) / 6
    end

    return D
end

"""
    growth_factor_LCDM(a, p::DFDParams_BG) -> Float64

Standard LCDM growth factor (scale-independent).
Uses k = 1e10 to force mu -> 1.
"""
function growth_factor_LCDM(a_final::Float64,
                             p::DFDParams_BG)::Float64
    return growth_factor_DFD(a_final, 1e10, p)
end

# ============================================================
# Sound horizon
# ============================================================

"""
    sound_horizon(p::DFDParams_BG) -> Float64

Sound horizon at the drag epoch in Mpc.
Eisenstein & Hu (1998) fitting formula.
"""
function sound_horizon(p::DFDParams_BG)::Float64
    omega_m = p.Omega_m0 * p.h^2
    omega_b = 0.02230  # Planck 2018 omega_b h^2

    z_d = 1060.0
    R_d = 31500.0 * omega_b * (2.726/2.7255)^(-4) / (1.0 + z_d)
    a_eq = 4.15e-5 / omega_m
    k_eq = 0.0746 * omega_m

    r_d = 2.0 / (3.0 * k_eq) * sqrt(6.0 / R_d) *
          log((sqrt(1 + R_d) + sqrt(R_d + 3.0*a_eq*(1+z_d))) /
              (1.0 + sqrt(3.0*a_eq*(1+z_d))))

    return r_d
end

end # module DFDBackground
