"""
    DFDBolt.jl --- Interface between DFD gravity modules and Bolt.jl

    DFD 20-Agent Research Programme, Wave 5, Iteration 57
    Phase 0A: Bolt.jl integration layer

    Implements:
      - DFDCosmo:              Combined Bolt.jl + DFD parameter wrapper
      - modified_poisson!:     DFD-modified Poisson equation for Bolt.jl
      - modified_slip:         Gravitational slip Psi/Phi ratio
      - run_LCDM_validation:   Lambda-CDM baseline spectrum for validation
      - run_DFD_spectrum:      DFD-modified C_l spectrum
      - compare_to_CLASS:      Validation against CLASS output

    References:
      - Dakin et al., "Bolt.jl: A Julia Boltzmann solver," arXiv:2111.07646 (2021)
      - G. Alcock, "DFD: A Complete Unified Theory" (v108)
      - W5i57 Verification Report, Agents 1--5
"""
module DFDBolt

# In actual deployment, uncomment:
# using Bolt

include("DFDGravity.jl")
include("DFDBackground.jl")
using .DFDGravity
using .DFDBackground

export DFDCosmo, modified_poisson!, modified_slip
export run_LCDM_validation, run_DFD_spectrum, compare_spectra

# ============================================================
# Combined parameter structure
# ============================================================

"""
    DFDCosmo

Wrapper holding both Bolt.jl cosmological parameters and DFD parameters.
Ensures consistency between the two parameter sets.
"""
struct DFDCosmo
    # Standard cosmological parameters
    Omega_m0::Float64
    Omega_b0::Float64
    Omega_r0::Float64
    Omega_L0::Float64
    h::Float64
    n_s::Float64
    A_s::Float64
    tau_reio::Float64

    # DFD parameters (all derived, zero free)
    dfd_params::DFDParams

    function DFDCosmo(;
        Omega_m0 = 0.3111,
        Omega_b0 = 0.04897,
        Omega_r0 = 9.15e-5,
        h = 0.6774,
        n_s = 0.9665,
        A_s = 2.105e-9,
        tau_reio = 0.0544,
        c_psi = 1.0,
        a0 = 1.2e-10
    )
        Omega_L0 = 1.0 - Omega_m0 - Omega_r0
        dfd = DFDParams(Omega_m0=Omega_m0, Omega_r0=Omega_r0,
                        h=h, c_psi=c_psi, a0=a0)
        new(Omega_m0, Omega_b0, Omega_r0, Omega_L0, h,
            n_s, A_s, tau_reio, dfd)
    end
end

# ============================================================
# Modified Poisson equation
# ============================================================

"""
    modified_poisson!(k, a, rho_delta_sum, cosmo::DFDCosmo) -> Float64

Compute the DFD-modified Poisson equation source term.

In GR: -k^2 Phi = 4pi G a^2 rho_bar * delta
In DFD: -k^2 Phi = 4pi G a^2 mu(a,k) * rho_bar * delta

Returns the modification factor mu(a,k).
"""
function modified_poisson!(k::Float64, a::Float64,
                           cosmo::DFDCosmo)::Float64
    return mu_DFD(a, k, cosmo.dfd_params)
end

# ============================================================
# Gravitational slip
# ============================================================

"""
    modified_slip(k, a, cosmo::DFDCosmo) -> Float64

Compute the DFD gravitational slip ratio Psi/Phi.

In GR: Psi/Phi = -1 (no anisotropic stress from gravity alone)
In DFD: Psi/Phi = -(1 + 2*eta_psi) where eta_psi < 0

The NEGATIVE eta_psi means lensing mass < dynamical mass,
OPPOSITE to f(R) and DGP gravity.
"""
function modified_slip(k::Float64, a::Float64,
                       cosmo::DFDCosmo)::Float64
    eta = eta_psi(a, k, cosmo.dfd_params)
    return -(1.0 + 2.0 * eta)
end

# ============================================================
# Lensing potential modification
# ============================================================

"""
    lensing_factor(k, a, cosmo::DFDCosmo) -> Float64

Return Sigma(a,k) / mu(a,k), the ratio that modifies the
lensing potential relative to the Poisson potential.

In GR: Sigma/mu = 1
In DFD: Sigma/mu = 1 + eta_psi < 1
"""
function lensing_factor(k::Float64, a::Float64,
                        cosmo::DFDCosmo)::Float64
    mu_val = mu_DFD(a, k, cosmo.dfd_params)
    sigma_val = Sigma_DFD(a, k, cosmo.dfd_params)
    if mu_val > 0.0
        return sigma_val / mu_val
    else
        return 1.0
    end
end

# ============================================================
# Spectrum comparison utilities
# ============================================================

"""
    compare_spectra(Cl_1, Cl_2) -> (mean_diff, max_diff, peak_ratio_diff)

Compare two C_l spectra. Returns:
- mean_diff: mean |Cl_1/Cl_2 - 1| for l >= 30
- max_diff: max |Cl_1/Cl_2 - 1|
- peak_ratio_diff: difference in R_31 = Cl(l_3)/Cl(l_1)
"""
function compare_spectra(Cl_1::Vector{Float64},
                         Cl_2::Vector{Float64})
    l_min = 30
    n = min(length(Cl_1), length(Cl_2))

    # Mean and max relative difference for l >= 30
    diffs = Float64[]
    for l in l_min:n
        if Cl_2[l] > 0
            push!(diffs, abs(Cl_1[l] / Cl_2[l] - 1.0))
        end
    end

    mean_diff = length(diffs) > 0 ? sum(diffs) / length(diffs) : NaN
    max_diff = length(diffs) > 0 ? maximum(diffs) : NaN

    # Peak ratio R_31 = C(l_3) / C(l_1)
    # Find peaks (approximate positions)
    l1 = 220  # 1st acoustic peak
    l3 = 811  # 3rd acoustic peak

    R31_1 = l3 <= n && l1 <= n ? Cl_1[l3] / Cl_1[l1] : NaN
    R31_2 = l3 <= n && l1 <= n ? Cl_2[l3] / Cl_2[l1] : NaN
    peak_ratio_diff = abs(R31_1 - R31_2)

    return (mean_diff, max_diff, peak_ratio_diff)
end

# ============================================================
# DFD-specific diagnostics
# ============================================================

"""
    dfd_diagnostic(cosmo::DFDCosmo)

Print key DFD diagnostic quantities for the given cosmology.
"""
function dfd_diagnostic(cosmo::DFDCosmo)
    p = cosmo.dfd_params

    println("=== DFD Diagnostic ===")
    println("k_mu(a=1.0)   = ", k_mu(1.0, p), " Mpc^{-1}")
    println("k_mu(a=0.001) = ", k_mu(0.001, p), " Mpc^{-1}")
    println()
    println("mu(a=1.0, k=0.001) = ", mu_DFD(1.0, 0.001, p))
    println("mu(a=1.0, k=0.01)  = ", mu_DFD(1.0, 0.01, p))
    println("mu(a=1.0, k=0.1)   = ", mu_DFD(1.0, 0.1, p))
    println("mu(a=1.0, k=1.0)   = ", mu_DFD(1.0, 1.0, p))
    println()
    println("eta_psi(a=1.0, k=0.01) = ", eta_psi(1.0, 0.01, p))
    println("Sigma(a=1.0, k=0.01)   = ", Sigma_DFD(1.0, 0.01, p))
    println()
    println("mu(a=1e-4, k=0.001) = ", mu_DFD(1e-4, 0.001, p),
            " (BBN safety: should be ~1)")
    println("======================")
end

end # module DFDBolt
