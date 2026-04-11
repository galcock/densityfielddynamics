#!/usr/bin/env python3
"""
DFD P(k) Confrontation Pipeline
================================
Analyzes BOSS DR12 / eBOSS DR16 power spectrum multipoles from Beutler et al.
(arXiv:2106.06324) deconvolved data products.

Usage:
    1. Download ps1D files from urls.txt (or fbeutler.github.io/hub/deconv_paper.html)
    2. Place them in a data/ subdirectory
    3. Run: python pk_analysis_pipeline.py

Measures:
    - P2/P0 ratio in linear regime (k = 0.02-0.15 h/Mpc)
    - Inverts Kaiser formula to get beta = f/b
    - Compares DFD prediction (G_eff -> G on linear scales => same as LCDM)
    - Produces publication-quality figure
"""

import numpy as np
import os
import glob
import sys

# ============================================================================
# Configuration
# ============================================================================
DATA_DIR = "data"  # put ps1D .dat files here
K_MIN = 0.02       # h/Mpc — avoid sample variance at very low k
K_MAX = 0.15       # h/Mpc — stay in linear regime
OUTPUT_FIG = "DFD_Pk_confrontation.png"

# Fiducial cosmology (Planck 2018 + DFD dictionary)
OMEGA_M_0 = 0.31
H0 = 67.36  # km/s/Mpc — Planck fiducial used by Beutler

# Galaxy bias priors from Beutler et al. Table 3
BIAS_PRIORS = {
    'z1': {'z_eff': 0.38, 'b': 2.01, 'b_err': 0.07},
    'z3': {'z_eff': 0.61, 'b': 2.13, 'b_err': 0.07},
    'QSO': {'z_eff': 1.52, 'b': 2.36, 'b_err': 0.12},
}

# ============================================================================
# Theory predictions
# ============================================================================
def omega_m_z(z, Om0=OMEGA_M_0):
    """Matter density parameter at redshift z (flat LCDM dictionary)."""
    return Om0 * (1+z)**3 / (Om0*(1+z)**3 + (1-Om0))

def growth_rate_f(z, gamma=0.55, Om0=OMEGA_M_0):
    """Linear growth rate f = Omega_m(z)^gamma.
    DFD prediction: identical to LCDM on linear scales because
    G_eff -> G when mu_0 -> 1 (high-acceleration / linear regime)."""
    return omega_m_z(z, Om0)**gamma

def beta_theory(z, b, gamma=0.55):
    """beta = f/b theoretical prediction."""
    return growth_rate_f(z, gamma) / b

def kaiser_P2_P0(beta):
    """Kaiser prediction for P2/P0 ratio."""
    num = (4./3)*beta + (4./7)*beta**2
    den = 1 + (2./3)*beta + (1./5)*beta**2
    return num / den

def invert_kaiser(r2):
    """Invert Kaiser formula: given r2 = P2/P0, solve for beta.
    Numerically solve: r2*(1 + 2/3*b + 1/5*b^2) = 4/3*b + 4/7*b^2
    => (4/7 - r2/5)*b^2 + (4/3 - 2*r2/3)*b - r2 = 0
    """
    a_coeff = 4./7 - r2/5
    b_coeff = 4./3 - 2*r2/3
    c_coeff = -r2
    discriminant = b_coeff**2 - 4*a_coeff*c_coeff
    if discriminant < 0:
        return np.nan
    beta = (-b_coeff + np.sqrt(discriminant)) / (2*a_coeff)
    return beta

# ============================================================================
# Data reading (Beutler ps1D format)
# ============================================================================
def read_ps1D(filepath):
    """Read a Beutler-format ps1D file.
    Format: columns are k, P0, P2, P4 (possibly more columns).
    Lines starting with # are comments.
    """
    data = np.loadtxt(filepath, comments='#')
    if data.ndim == 1:
        raise ValueError(f"Only 1 row in {filepath}")
    
    k = data[:, 0]
    P0 = data[:, 1]
    P2 = data[:, 2] if data.shape[1] > 2 else np.zeros_like(k)
    P4 = data[:, 3] if data.shape[1] > 3 else np.zeros_like(k)
    
    return k, P0, P2, P4

def find_data_files(data_dir):
    """Find and categorize ps1D files."""
    samples = {}
    
    patterns = {
        'BOSS_z1_NGC': '*BOSS_DR12_NGC_z1_COMPnbar*renorm*',
        'BOSS_z1_SGC': '*BOSS_DR12_SGC_z1_COMPnbar*renorm*',
        'BOSS_z3_NGC': '*BOSS_DR12_NGC_z3_COMPnbar*renorm*',
        'BOSS_z3_SGC': '*BOSS_DR12_SGC_z3_COMPnbar*renorm*',
        'eBOSS_QSO_NGC': '*eBOSS_DR16_QSO_NGC*renorm*',
        'eBOSS_QSO_SGC': '*eBOSS_DR16_QSO_SGC*renorm*',
    }
    
    for name, pattern in patterns.items():
        files = glob.glob(os.path.join(data_dir, pattern))
        if files:
            samples[name] = files[0]
            print(f"  Found {name}: {os.path.basename(files[0])}")
        else:
            print(f"  MISSING {name}: no file matching {pattern}")
    
    return samples

# ============================================================================
# Analysis
# ============================================================================
def measure_beta(k, P0, P2, k_min=K_MIN, k_max=K_MAX):
    """Measure beta from P2/P0 ratio in the linear regime."""
    mask = (k >= k_min) & (k <= k_max) & (P0 > 0) & np.isfinite(P2) & np.isfinite(P0)
    
    if mask.sum() < 3:
        return np.nan, np.nan
    
    k_lin = k[mask]
    P0_lin = P0[mask]
    P2_lin = P2[mask]
    
    # Weighted mean of r2 = P2/P0 (weight by P0 as proxy for S/N)
    r2_vals = P2_lin / P0_lin
    weights = P0_lin  # larger P0 = better S/N
    
    r2_mean = np.average(r2_vals, weights=weights)
    r2_err = np.sqrt(np.average((r2_vals - r2_mean)**2, weights=weights)) / np.sqrt(mask.sum())
    
    beta = invert_kaiser(r2_mean)
    
    # Error propagation via finite differences
    beta_hi = invert_kaiser(r2_mean + r2_err)
    beta_lo = invert_kaiser(r2_mean - r2_err)
    beta_err = abs(beta_hi - beta_lo) / 2
    
    return beta, beta_err

def combine_NGC_SGC(beta_N, err_N, beta_S, err_S):
    """Inverse-variance weighted combination of NGC + SGC."""
    if np.isnan(beta_N) or np.isnan(beta_S):
        if np.isnan(beta_N):
            return beta_S, err_S
        return beta_N, err_N
    
    w_N = 1./err_N**2
    w_S = 1./err_S**2
    beta_comb = (w_N*beta_N + w_S*beta_S) / (w_N + w_S)
    err_comb = 1./np.sqrt(w_N + w_S)
    return beta_comb, err_comb

# ============================================================================
# Main
# ============================================================================
def main():
    print("=" * 60)
    print("DFD P(k) Confrontation Pipeline")
    print("Data: Beutler et al. (2021) BOSS DR12 + eBOSS DR16")
    print("=" * 60)
    
    # Find data files
    print(f"\nSearching {DATA_DIR}/...")
    samples = find_data_files(DATA_DIR)
    
    if not samples:
        print("\nNo data files found!")
        print("Download ps1D files from urls.txt and place in data/ directory.")
        print("Key files needed (pre-reconstruction, for RSD measurement):")
        print("  ps1D_BOSS_DR12_NGC_z1_COMPnbar_TSC_700_700_700_400_renorm.dat")
        print("  ps1D_BOSS_DR12_SGC_z1_COMPnbar_TSC_700_700_700_400_renorm.dat")
        print("  ps1D_BOSS_DR12_NGC_z3_COMPnbar_TSC_700_700_700_400_renorm.dat")
        print("  ps1D_BOSS_DR12_SGC_z3_COMPnbar_TSC_700_700_700_400_renorm.dat")
        print("  ps1D_eBOSS_DR16_QSO_NGC_TSC_0.8_2.2_1270_1270_1270_400_renorm.dat")
        print("  ps1D_eBOSS_DR16_QSO_SGC_TSC_0.8_2.2_1040_1040_1040_400_renorm.dat")
        return
    
    # Analyze each sample
    results = {}
    
    for name, filepath in samples.items():
        print(f"\nAnalyzing {name}...")
        k, P0, P2, P4 = read_ps1D(filepath)
        print(f"  k range: [{k.min():.4f}, {k.max():.4f}] h/Mpc, {len(k)} bins")
        
        beta, beta_err = measure_beta(k, P0, P2)
        results[name] = {'beta': beta, 'beta_err': beta_err, 'k': k, 'P0': P0, 'P2': P2, 'P4': P4}
        print(f"  beta = {beta:.3f} +/- {beta_err:.3f}")
    
    # Combine NGC + SGC
    print("\n" + "=" * 60)
    print("Combined NGC+SGC results")
    print("=" * 60)
    
    combined = {}
    for zbin, label, bias_key in [
        ('z1', 'BOSS z=0.2-0.5', 'z1'),
        ('z3', 'BOSS z=0.5-0.75', 'z3'),
        ('QSO', 'eBOSS QSO', 'QSO'),
    ]:
        ngc_key = f'BOSS_{zbin}_NGC' if 'z' in zbin else f'eBOSS_{zbin}_NGC'
        sgc_key = f'BOSS_{zbin}_SGC' if 'z' in zbin else f'eBOSS_{zbin}_SGC'
        
        b_N = results.get(ngc_key, {}).get('beta', np.nan)
        e_N = results.get(ngc_key, {}).get('beta_err', np.inf)
        b_S = results.get(sgc_key, {}).get('beta', np.nan)
        e_S = results.get(sgc_key, {}).get('beta_err', np.inf)
        
        beta_c, err_c = combine_NGC_SGC(b_N, e_N, b_S, e_S)
        
        bp = BIAS_PRIORS[bias_key]
        beta_th = beta_theory(bp['z_eff'], bp['b'])
        f_th = growth_rate_f(bp['z_eff'])
        
        combined[zbin] = {
            'label': label, 'z_eff': bp['z_eff'],
            'beta_meas': beta_c, 'beta_err': err_c,
            'beta_th': beta_th, 'f_th': f_th, 'b': bp['b'],
        }
        
        print(f"\n{label} (z_eff = {bp['z_eff']}):")
        print(f"  beta_meas = {beta_c:.3f} +/- {err_c:.3f}")
        print(f"  beta_th   = {beta_th:.3f}  (f={f_th:.3f}, b={bp['b']:.2f})")
        tension = abs(beta_c - beta_th) / np.sqrt(err_c**2 + (bp['b_err']*f_th/bp['b']**2)**2)
        print(f"  tension   = {tension:.1f} sigma")
    
    # DFD interpretation
    print("\n" + "=" * 60)
    print("DFD Interpretation")
    print("=" * 60)
    print("""
On BOSS/eBOSS linear scales (k < 0.15 h/Mpc), the DFD growth rate is:

  G_eff = G / [mu_0 * (1 + L_0 * mu_k^2)]

For the linear cosmological regime (x_bar >> 1):
  mu_0 -> 1,  L_0 -> 0,  so G_eff -> G

Therefore DFD predicts IDENTICAL linear growth to LCDM.
The P(k) confrontation tests consistency, not distinctiveness.
DFD's signatures appear in the nonlinear/galactic regime, not here.
""")
    
    # Generate figure
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Left panel: example P0, P2, P4
        first_key = list(results.keys())[0]
        r = results[first_key]
        ax = axes[0]
        mask = r['k'] > 0.005
        ax.loglog(r['k'][mask], r['P0'][mask], 'C0-', lw=1.5, label='$P_0$')
        ax.loglog(r['k'][mask], np.abs(r['P2'][mask]), 'C1-', lw=1.2, label='$|P_2|$')
        ax.set_xlabel('$k$ [$h$/Mpc]')
        ax.set_ylabel('$P_\\ell(k)$ [(Mpc/$h$)$^3$]')
        ax.set_title(f'Power spectrum multipoles ({first_key})')
        ax.legend()
        ax.set_xlim(0.005, 0.3)
        
        # Right panel: beta vs z
        ax = axes[1]
        z_arr = np.linspace(0.1, 2.0, 100)
        for b_val in [1.8, 2.0, 2.2, 2.4]:
            beta_arr = [beta_theory(z, b_val) for z in z_arr]
            ax.plot(z_arr, beta_arr, 'C0-', alpha=0.15)
        
        # Theory band (b = 2.0 +/- 0.2)
        beta_hi = [beta_theory(z, 1.8) for z in z_arr]
        beta_lo = [beta_theory(z, 2.4) for z in z_arr]
        ax.fill_between(z_arr, beta_lo, beta_hi, color='C0', alpha=0.15, label='DFD/ΛCDM (b=1.8–2.4)')
        beta_mid = [beta_theory(z, 2.1) for z in z_arr]
        ax.plot(z_arr, beta_mid, 'C0-', lw=2, label='DFD/ΛCDM (b=2.1)')
        
        colors = ['C1', 'C2', 'C3']
        for i, (zbin, c) in enumerate(zip(combined, colors)):
            d = combined[zbin]
            ax.errorbar(d['z_eff'], d['beta_meas'], yerr=d['beta_err'],
                       fmt='o', color=c, ms=8, capsize=4, label=d['label'])
        
        ax.set_xlabel('Redshift $z$')
        ax.set_ylabel('$\\beta = f/b$')
        ax.set_title('RSD parameter: DFD vs BOSS/eBOSS')
        ax.legend(fontsize=8)
        ax.set_xlim(0, 2.0)
        ax.set_ylim(0, 0.6)
        
        plt.tight_layout()
        plt.savefig(OUTPUT_FIG, dpi=200, bbox_inches='tight')
        print(f"\nFigure saved to {OUTPUT_FIG}")
    except ImportError:
        print("\nmatplotlib not available; skipping figure generation.")
    
    # Output table for LaTeX
    print("\n" + "=" * 60)
    print("LaTeX table")
    print("=" * 60)
    print(r"\begin{tabular}{lccc}")
    print(r"\toprule")
    print(r"Sample & $z_{\rm eff}$ & $\beta_{\rm meas}$ & $\beta_{\rm DFD/\Lambda CDM}$ \\")
    print(r"\midrule")
    for zbin in combined:
        d = combined[zbin]
        print(f"{d['label']} & {d['z_eff']:.2f} & ${d['beta_meas']:.3f} \\pm {d['beta_err']:.3f}$ & {d['beta_th']:.3f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

if __name__ == '__main__':
    main()
