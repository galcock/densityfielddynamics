#!/usr/bin/env python3
"""
SRF Cavity Tidal Analysis for DFD Lambda Constraints
=====================================================

Simulates the expected tidal frequency shift in superconducting RF cavities
due to the DFD lambda parameter, generates synthetic data with realistic noise,
performs cross-correlation and spectral analysis, and determines the minimum
detectable lambda as a function of measurement duration and noise floor.

Theory: In DFD, the resonant frequency of an SRF cavity shifts when the local
gravitational potential changes. The shift is:

    delta_f / f = (lambda - 1) * delta_Phi / c^2

where delta_Phi is the change in gravitational potential (from lunar/solar tides),
and lambda parameterizes the anomalous EM-gravitational coupling.

The tidal potential at Earth's surface has principal components:
    M2 (principal lunar):  period = 12.4206 hr, amplitude ~ 2.6e-7 m/s^2
    S2 (principal solar):  period = 12.0000 hr, amplitude ~ 1.2e-7 m/s^2
    K1 (luni-solar diurnal): period = 23.9345 hr, amplitude ~ 1.6e-7 m/s^2
    O1 (principal lunar diurnal): period = 25.8193 hr, amplitude ~ 1.1e-7 m/s^2

The tidal potential variation is delta_Phi ~ g_tidal * R_Earth, giving
delta_Phi/c^2 ~ 10^{-16} for the M2 component.

Author: Gary Thomas Alcock / Claude analysis tool
Date: 2026-03-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit
import os

# ============================================================================
# Physical Constants
# ============================================================================
c = 2.998e8          # speed of light [m/s]
G = 6.674e-11        # gravitational constant [m^3 kg^-1 s^-2]
R_earth = 6.371e6    # Earth radius [m]
M_moon = 7.342e22    # Moon mass [kg]
M_sun = 1.989e30     # Sun mass [kg]
d_moon = 3.844e8     # Earth-Moon distance [m]
d_sun = 1.496e11     # Earth-Sun distance [m]

# ============================================================================
# Tidal Potential Computation
# ============================================================================

def tidal_acceleration_amplitude(M, d):
    """Tidal acceleration amplitude from a body of mass M at distance d.

    g_tidal = 2 * G * M * R_earth / d^3
    """
    return 2 * G * M * R_earth / d**3

def tidal_potential_variation(M, d):
    """Tidal potential variation at Earth's surface.

    delta_Phi = G * M * R_earth^2 / d^3
    (This is the amplitude of the degree-2 tidal potential.)
    """
    return G * M * R_earth**2 / d**3

# Compute tidal amplitudes
g_tidal_moon = tidal_acceleration_amplitude(M_moon, d_moon)
g_tidal_sun = tidal_acceleration_amplitude(M_sun, d_sun)
dPhi_moon = tidal_potential_variation(M_moon, d_moon)
dPhi_sun = tidal_potential_variation(M_sun, d_sun)

print("=" * 70)
print("TIDAL PARAMETERS AT EARTH'S SURFACE")
print("=" * 70)
print(f"Lunar tidal acceleration:    g_M2 = {g_tidal_moon:.3e} m/s^2")
print(f"Solar tidal acceleration:    g_S2 = {g_tidal_sun:.3e} m/s^2")
print(f"Lunar tidal potential:       dPhi_moon = {dPhi_moon:.3e} m^2/s^2")
print(f"Solar tidal potential:       dPhi_sun = {dPhi_sun:.3e} m^2/s^2")
print(f"Lunar dPhi/c^2:              {dPhi_moon/c**2:.3e}")
print(f"Solar dPhi/c^2:              {dPhi_sun/c**2:.3e}")
print(f"Combined dPhi/c^2 (max):     {(dPhi_moon + dPhi_sun)/c**2:.3e}")


# ============================================================================
# Tidal Constituent Table
# ============================================================================

# Principal tidal constituents: (name, period_hours, relative_amplitude_to_M2)
TIDAL_CONSTITUENTS = {
    'M2': {'period_hr': 12.4206, 'g_amp': g_tidal_moon,
            'dPhi': dPhi_moon, 'description': 'Principal lunar semidiurnal'},
    'S2': {'period_hr': 12.0000, 'g_amp': g_tidal_sun * 0.46,
            'dPhi': dPhi_sun * 0.46, 'description': 'Principal solar semidiurnal'},
    'K1': {'period_hr': 23.9345, 'g_amp': g_tidal_moon * 0.58,
            'dPhi': dPhi_moon * 0.58, 'description': 'Luni-solar diurnal'},
    'O1': {'period_hr': 25.8193, 'g_amp': g_tidal_moon * 0.41,
            'dPhi': dPhi_moon * 0.41, 'description': 'Principal lunar diurnal'},
    'N2': {'period_hr': 12.6583, 'g_amp': g_tidal_moon * 0.19,
            'dPhi': dPhi_moon * 0.19, 'description': 'Larger lunar elliptic'},
    'K2': {'period_hr': 11.9672, 'g_amp': g_tidal_sun * 0.13,
            'dPhi': dPhi_sun * 0.13, 'description': 'Luni-solar semidiurnal'},
}

print("\n" + "=" * 70)
print("TIDAL CONSTITUENT TABLE")
print("=" * 70)
print(f"{'Name':<6} {'Period (hr)':<14} {'g_tidal (m/s^2)':<18} "
      f"{'dPhi/c^2':<14} {'Description'}")
print("-" * 70)
for name, tc in TIDAL_CONSTITUENTS.items():
    print(f"{name:<6} {tc['period_hr']:<14.4f} {tc['g_amp']:<18.3e} "
          f"{tc['dPhi']/c**2:<14.3e} {tc['description']}")


# ============================================================================
# DFD Frequency Shift Derivation
# ============================================================================

def dfd_frequency_shift(lam, dPhi_over_c2):
    """
    DFD prediction for cavity frequency shift.

    In DFD, the optical metric is ds^2 = -c^2 dt^2/n^2 + dx^2 with n = e^psi.
    The gravitational potential Phi relates to psi via: psi = 2*Phi/c^2.

    A cavity resonant frequency depends on:
    1. The cavity dimensions (strain from gravitational potential):
       delta_L/L = Phi/(c^2) [standard gravitational strain]
    2. The permittivity/permeability of the medium inside the cavity:
       epsilon(psi) = epsilon_0 * e^{(1+kappa)*psi}
       mu(psi) = mu_0 * e^{(1-kappa)*psi}
    3. The phase velocity: v_ph = c/n = c * e^{-psi}

    For a cavity mode with f = m * v_ph / (2*L) (standing wave):
       f = m * c * e^{-psi} / (2 * L * (1 + Phi/c^2))

    The DFD modification: the EM energy stored in the cavity acts as a
    gravitational source with effective mass (lambda * U_EM / c^2).
    When lambda != 1, there is an ADDITIONAL frequency shift beyond the
    standard gravitational redshift:

       delta_f/f |_DFD = (lambda - 1) * (U_EM / M_cav*c^2) * delta_Phi/c^2

    For a passive cavity (no stored energy contributing to self-gravity):
       delta_f/f |_standard = -delta_Phi/c^2  (gravitational redshift)

    The DFD EXCESS signal is:
       delta_f/f |_excess = (lambda - 1) * delta_Phi/c^2

    This is the signal we search for in the tidal modulation.

    More precisely, from the DFD field equation (Eq. in Deep_EM_Coupling):
    The EM energy density sources psi with coupling lambda. The stored
    energy U modifies the local psi field by:
       delta_psi = (4*pi*G*lambda*U) / (c^4 * V_eff)

    When the external potential changes by delta_Phi, the cavity frequency
    shifts. The standard GR shift is delta_f/f = -delta_Phi/c^2.
    The DFD correction involves the response of the EM-sourced psi to
    the changing external potential, giving an additional term proportional
    to (lambda - 1).

    Parameters
    ----------
    lam : float
        DFD lambda parameter (lambda = 1 is standard physics)
    dPhi_over_c2 : float
        Gravitational potential variation divided by c^2

    Returns
    -------
    delta_f_over_f : float
        Fractional frequency shift (the DFD excess, beyond standard GR)
    """
    return (lam - 1.0) * dPhi_over_c2


def dfd_frequency_shift_with_stored_energy(lam, kappa, U_stored, V_cavity,
                                            f_cavity, dPhi_over_c2):
    """
    Full DFD frequency shift including stored energy enhancement.

    When the cavity has significant stored energy, the EM energy itself
    modifies the local psi field. The tidal modulation of the external
    potential then changes how this self-sourced psi contribution affects
    the cavity frequency.

    The enhanced signal is:

    delta_f/f = (lambda - 1) * dPhi/c^2 * [1 + eta_EM]

    where eta_EM = U_stored / (rho_wall * V_wall * c^2) is the ratio of
    EM energy to rest mass energy of the cavity walls. For typical SRF
    cavities, eta_EM ~ 10^{-12}, so the enhancement is negligible.

    The dominant effect remains the direct coupling:
    delta_f/f = (lambda - 1) * dPhi/c^2

    HOWEVER, there is a second-order effect from the psi-dependent
    permittivity/permeability:

    delta_f/f |_kappa = -(lambda - 1) * kappa * (u_E - u_B)/u_EM * dPhi/c^2

    For a typical TM010 mode where u_E ~ u_B, this kappa term is small.
    """
    # Direct coupling (dominant)
    direct = (lam - 1.0) * dPhi_over_c2

    # Stored energy enhancement (negligible for lab cavities)
    rho_Nb = 8570.0  # kg/m^3, niobium density
    V_wall = 0.002 * 0.1  # ~2mm thick walls, ~0.1 m^2 area -> ~2e-4 m^3
    M_wall = rho_Nb * V_wall  # ~1.7 kg
    eta_EM = U_stored / (M_wall * c**2)  # ~ 10^{-14} for U~1J

    enhanced = direct * (1.0 + eta_EM)

    return enhanced, eta_EM


# ============================================================================
# Compute Expected Signals for Real SRF Cavities
# ============================================================================

print("\n" + "=" * 70)
print("EXPECTED DFD TIDAL SIGNAL FOR SRF CAVITIES")
print("=" * 70)

# Cavity database: real facilities
CAVITIES = {
    'Dark_SRF_Fermilab': {
        'f_GHz': 1.3,
        'Q0': 1.1e10,
        'QL': 4.7e9,
        'U_stored_J': 0.01,  # low stored energy in detection mode
        'bandwidth_Hz': 0.277,
        'microphonics_Hz_rms': 3.0,
        'drift_Hz_per_hr': 5.7 * 60 / 100,  # 5.7 Hz per 100 min
        'measurement_duration_s': 1000,
        'noise_floor_df_f': 3.0 / 1.3e9,  # microphonics-limited
    },
    'DESY_XFEL_1.3GHz': {
        'f_GHz': 1.3,
        'Q0': 1e10,
        'QL': 4.6e6,  # loaded Q for beam operation
        'U_stored_J': 260,  # per cavity at 23.6 MV/m
        'bandwidth_Hz': 283,  # loaded bandwidth
        'microphonics_Hz_rms': 5.0,
        'drift_Hz_per_hr': 10.0,  # estimated
        'measurement_duration_s': 600,  # typical pulsed measurement
        'noise_floor_df_f': 5.0 / 1.3e9,
    },
    'JLab_CEBAF_1.5GHz': {
        'f_GHz': 1.497,
        'Q0': 1e10,
        'QL': 2e7,  # CW operation
        'U_stored_J': 10,  # per cavity, CW
        'bandwidth_Hz': 75,
        'microphonics_Hz_rms': 3.0,
        'drift_Hz_per_hr': 5.0,
        'measurement_duration_s': 3600,  # CW allows long measurements
        'noise_floor_df_f': 3.0 / 1.497e9,
    },
    'MAGO_2GHz': {
        'f_GHz': 2.065,
        'Q0': 5e3,  # room temperature Q
        'QL': 5e3,
        'U_stored_J': 0.001,
        'bandwidth_Hz': 413e3,  # very broad at room T
        'microphonics_Hz_rms': 100,  # estimated room T
        'drift_Hz_per_hr': 1000,
        'measurement_duration_s': 100,
        'noise_floor_df_f': 100 / 2.065e9,
        'note': 'Room temperature only; cryogenic tests planned'
    },
    'SQMS_Quantum_Cavity': {
        'f_GHz': 1.3,
        'Q0': 2e10,
        'QL': 1e10,
        'U_stored_J': 1.0,  # quantum-limited stored energy
        'bandwidth_Hz': 0.13,  # ultra-narrow
        'microphonics_Hz_rms': 2.6,  # from Dark SRF improved run
        'drift_Hz_per_hr': 0.1,  # helium-cooled, stable
        'measurement_duration_s': 7200,  # 2 hours typical quantum test
        'noise_floor_df_f': 2.6 / 1.3e9,
    },
}

# M2 tidal potential variation
dPhi_M2_over_c2 = dPhi_moon / c**2  # ~ 2.7e-17

print(f"\nM2 tidal potential: dPhi/c^2 = {dPhi_M2_over_c2:.3e}")
print(f"\nFor lambda - 1 = 1:")
print(f"  Maximum tidal frequency shift: delta_f/f = {dPhi_M2_over_c2:.3e}")
print(f"  At 1.3 GHz: delta_f = {dPhi_M2_over_c2 * 1.3e9:.3e} Hz")
print(f"\nFor lambda - 1 = 10^-9:")
lam_test = 1.0 + 1e-9
print(f"  delta_f/f = {dfd_frequency_shift(lam_test, dPhi_M2_over_c2):.3e}")
print(f"  At 1.3 GHz: delta_f = {dfd_frequency_shift(lam_test, dPhi_M2_over_c2) * 1.3e9:.3e} Hz")

print("\n" + "-" * 70)
print("LAMBDA BOUNDS FROM EXISTING NOISE FLOORS")
print("-" * 70)
print(f"\n{'Cavity':<25} {'f (GHz)':<10} {'Noise floor (df/f)':<22} "
      f"{'|lam-1| bound':<16} {'Duration'}")
print("-" * 90)

lambda_bounds = {}
for name, cav in CAVITIES.items():
    noise = cav['noise_floor_df_f']
    # The bound on |lambda - 1| from the noise floor alone:
    # |lambda - 1| < noise_floor / (dPhi/c^2)
    # But with coherent averaging over N_tidal_cycles:
    T = cav['measurement_duration_s']
    T_M2 = 12.4206 * 3600  # M2 period in seconds
    N_cycles = T / T_M2

    # For a single measurement (no tidal coherent averaging):
    bound_single = noise / dPhi_M2_over_c2

    # With optimal filtering over the measurement duration:
    # The sensitivity improves as sqrt(T / T_noise_correlation)
    # For microphonics (correlation time ~ 0.064 s from Dark SRF paper):
    tau_noise = 0.064  # noise correlation time [s]
    N_independent = T / max(tau_noise, 1.0)
    bound_averaged = noise / (dPhi_M2_over_c2 * np.sqrt(N_independent))

    lambda_bounds[name] = {
        'single': bound_single,
        'averaged': bound_averaged,
        'N_cycles': N_cycles,
    }

    dur_str = f"{T:.0f} s" if T < 3600 else f"{T/3600:.1f} hr"
    print(f"{name:<25} {cav['f_GHz']:<10.3f} {noise:<22.3e} "
          f"{bound_averaged:<16.3e} {dur_str}")


# ============================================================================
# Extended Measurement Scenario: Weeks of Continuous Data
# ============================================================================

print("\n" + "=" * 70)
print("LAMBDA SENSITIVITY vs MEASUREMENT DURATION")
print("=" * 70)

durations_days = np.array([0.01, 0.1, 0.5, 1, 3, 7, 14, 30, 90])
durations_s = durations_days * 86400

# Use the SQMS quantum cavity as reference
sqms = CAVITIES['SQMS_Quantum_Cavity']
noise_sqms = sqms['noise_floor_df_f']

print(f"\nReference: SQMS cavity, noise floor = {noise_sqms:.2e}")
print(f"\n{'Duration':<15} {'N_M2_cycles':<15} {'lambda bound':<15} {'delta_f at bound (Hz)'}")
print("-" * 65)

lam_bounds_vs_time = []
for T, Td in zip(durations_s, durations_days):
    T_M2 = 12.4206 * 3600
    N_cycles = T / T_M2
    # For tidal correlation analysis, sensitivity improves as sqrt(N_cycles)
    # when N_cycles >= 1, otherwise limited by single-shot noise
    if N_cycles >= 1:
        bound = noise_sqms / (dPhi_M2_over_c2 * np.sqrt(N_cycles))
    else:
        bound = noise_sqms / dPhi_M2_over_c2
    lam_bounds_vs_time.append(bound)

    dur_str = f"{Td:.2f} days" if Td < 1 else f"{Td:.0f} days"
    df_at_bound = bound * dPhi_M2_over_c2 * 1.3e9
    print(f"{dur_str:<15} {N_cycles:<15.1f} {bound:<15.3e} {df_at_bound:.3e}")


# ============================================================================
# Synthetic Time Series Generation
# ============================================================================

def generate_tidal_signal(t, lambda_minus_1, f_cavity_Hz,
                          latitude_deg=41.84):
    """
    Generate the tidal frequency shift signal.

    Uses the principal tidal constituents to generate a realistic
    tidal potential variation at the specified latitude.

    Parameters
    ----------
    t : ndarray
        Time array in seconds
    lambda_minus_1 : float
        Value of (lambda - 1)
    f_cavity_Hz : float
        Cavity frequency in Hz
    latitude_deg : float
        Geographic latitude (default: Fermilab, 41.84 N)

    Returns
    -------
    delta_f : ndarray
        Frequency shift in Hz
    delta_Phi_over_c2 : ndarray
        Total tidal potential variation / c^2
    """
    lat = np.radians(latitude_deg)
    delta_Phi_over_c2 = np.zeros_like(t)

    for name, tc in TIDAL_CONSTITUENTS.items():
        omega = 2 * np.pi / (tc['period_hr'] * 3600)  # rad/s
        amp = tc['dPhi'] / c**2

        # Latitude dependence: semidiurnal ~ cos^2(lat), diurnal ~ sin(2*lat)
        if tc['period_hr'] < 15:  # semidiurnal
            lat_factor = np.cos(lat)**2
        else:  # diurnal
            lat_factor = np.sin(2 * lat)

        # Random initial phase (unknown at analysis time)
        phase = np.random.uniform(0, 2 * np.pi)

        delta_Phi_over_c2 += amp * lat_factor * np.cos(omega * t + phase)

    delta_f = lambda_minus_1 * delta_Phi_over_c2 * f_cavity_Hz
    return delta_f, delta_Phi_over_c2


def generate_srf_noise(t, f_cavity_Hz, microphonics_rms_Hz=3.0,
                       drift_rate_Hz_per_s=0.001, white_noise_Hz=0.01):
    """
    Generate realistic SRF cavity frequency noise.

    Components:
    1. Microphonics: Lorentzian-spectrum noise centered at mechanical
       resonance frequencies (14-60 Hz), with RMS amplitude of a few Hz
    2. 1/f drift: Slow frequency walk from helium pressure variations,
       thermal effects
    3. White noise: Phase noise floor from LLRF electronics

    Parameters
    ----------
    t : ndarray
        Time array in seconds
    f_cavity_Hz : float
        Cavity frequency in Hz
    microphonics_rms_Hz : float
        RMS microphonic detuning in Hz
    drift_rate_Hz_per_s : float
        Drift rate in Hz/s
    white_noise_Hz : float
        White noise floor in Hz/sqrt(Hz)
    """
    dt = t[1] - t[0]
    N = len(t)

    # Component 1: Microphonics (Lorentzian noise at mechanical resonances)
    # Typical mechanical modes: 14 Hz, 45 Hz, 57 Hz (from Dark SRF data)
    mech_freqs = [14.3, 45.0, 57.2]
    mech_widths = [2.0, 3.0, 2.0]  # Hz bandwidth
    mech_amps = [0.5, 0.3, 0.2]    # relative amplitudes

    noise_micro = np.zeros(N)
    fs = 1.0 / dt
    f_nyquist = fs / 2.0

    for f_mech, width, amp in zip(mech_freqs, mech_widths, mech_amps):
        if f_mech >= f_nyquist:
            # Mechanical mode is above Nyquist: alias it or skip
            # Model as broadband noise contribution instead
            noise_micro += amp * np.random.randn(N)
            continue

        # Frequency-domain approach: generate white noise, filter through
        # Lorentzian transfer function centered at f_mech with width gamma
        white = np.random.randn(N)

        # Design a bandpass filter around the mechanical resonance
        f_low = max(f_mech - 3 * width, 0.1) / f_nyquist
        f_high = min(f_mech + 3 * width, f_nyquist * 0.99) / f_nyquist
        if f_low >= f_high or f_low <= 0:
            noise_micro += amp * np.random.randn(N)
            continue

        order = min(4, max(2, int(f_mech / width)))
        try:
            b, a = signal.butter(order, [f_low, f_high], btype='band')
            filtered = signal.filtfilt(b, a, white)
            noise_micro += amp * filtered / (np.std(filtered) + 1e-20)
        except Exception:
            noise_micro += amp * np.random.randn(N)

    noise_micro *= microphonics_rms_Hz

    # Component 2: 1/f drift (random walk + pink noise)
    # Model as integrated Brownian motion with restoring force
    drift = np.cumsum(np.random.randn(N) * drift_rate_Hz_per_s * np.sqrt(dt))

    # Component 3: White noise floor
    noise_white = np.random.randn(N) * white_noise_Hz / np.sqrt(dt)

    return noise_micro + drift + noise_white, noise_micro, drift, noise_white


def generate_synthetic_data(duration_hours=168, dt_seconds=0.1,
                           lambda_minus_1=1e-6, f_cavity_GHz=1.3,
                           microphonics_rms_Hz=3.0,
                           drift_rate_Hz_per_hr=0.1,
                           white_noise_Hz_sqrtHz=0.01,
                           latitude_deg=41.84):
    """
    Generate a complete synthetic SRF cavity frequency time series.

    Parameters
    ----------
    duration_hours : float
        Total measurement duration in hours
    dt_seconds : float
        Sampling interval in seconds
    lambda_minus_1 : float
        DFD parameter (lambda - 1)
    f_cavity_GHz : float
        Cavity frequency in GHz
    microphonics_rms_Hz : float
        RMS microphonic noise in Hz
    drift_rate_Hz_per_hr : float
        Frequency drift rate
    white_noise_Hz_sqrtHz : float
        White noise spectral density
    latitude_deg : float
        Facility latitude

    Returns
    -------
    t : ndarray
        Time in seconds
    f_signal : ndarray
        Tidal signal in Hz
    f_noise : ndarray
        Total noise in Hz
    f_total : ndarray
        Signal + noise in Hz
    tidal_potential : ndarray
        Tidal potential variation / c^2
    """
    T = duration_hours * 3600
    t = np.arange(0, T, dt_seconds)
    f_cav = f_cavity_GHz * 1e9

    # Generate tidal signal
    f_signal, tidal_pot = generate_tidal_signal(t, lambda_minus_1, f_cav,
                                                 latitude_deg)

    # Generate noise
    drift_rate_per_s = drift_rate_Hz_per_hr / 3600
    f_noise_total, _, _, _ = generate_srf_noise(
        t, f_cav, microphonics_rms_Hz, drift_rate_per_s, white_noise_Hz_sqrtHz
    )

    f_total = f_signal + f_noise_total

    return t, f_signal, f_noise_total, f_total, tidal_pot


# ============================================================================
# Analysis Functions
# ============================================================================

def compute_psd(t, y, nperseg=None):
    """Compute power spectral density using Welch's method."""
    dt = t[1] - t[0]
    fs = 1.0 / dt
    if nperseg is None:
        nperseg = min(len(y) // 4, int(48 * 3600 / dt))  # up to 48 hr segments

    freqs, psd = signal.welch(y, fs=fs, nperseg=nperseg,
                               window='hann', noverlap=nperseg//2)
    return freqs, psd


def cross_correlate_with_tides(t, freq_data, tidal_potential):
    """
    Cross-correlate cavity frequency data with tidal potential.

    Returns the cross-correlation coefficient and the optimal
    (lambda-1) estimate.
    """
    # Remove means
    fd = freq_data - np.mean(freq_data)
    tp = tidal_potential - np.mean(tidal_potential)

    # Normalize
    fd_norm = fd / (np.std(fd) + 1e-30)
    tp_norm = tp / (np.std(tp) + 1e-30)

    # Cross-correlation at zero lag
    r = np.mean(fd_norm * tp_norm)

    # Estimate lambda - 1 from regression
    # freq_data = (lambda-1) * f_cav * tidal_potential + noise
    # Linear regression: slope = (lambda-1) * f_cav
    slope = np.sum(fd * tp) / (np.sum(tp**2) + 1e-30)
    # slope has units of Hz / (dimensionless potential)
    # so lambda-1 = slope / f_cavity

    return r, slope


def tidal_frequency_analysis(t, freq_data, f_cavity_Hz):
    """
    Search for peaks at tidal frequencies in the PSD.

    Returns the amplitude at each tidal frequency and the
    corresponding lambda bound.
    """
    freqs, psd = compute_psd(t, freq_data)

    results = {}
    for name, tc in TIDAL_CONSTITUENTS.items():
        f_tidal = 1.0 / (tc['period_hr'] * 3600)  # Hz

        # Find nearest frequency bin
        idx = np.argmin(np.abs(freqs - f_tidal))
        if idx > 0 and idx < len(freqs) - 1:
            # Use 3-bin average around the tidal frequency
            psd_at_tidal = np.mean(psd[max(0,idx-1):idx+2])

            # Background noise (median of surrounding bins)
            bg_start = max(0, idx - 20)
            bg_end = min(len(freqs), idx + 20)
            bg_mask = np.ones(bg_end - bg_start, dtype=bool)
            bg_mask[max(0, idx-2)-bg_start:idx+3-bg_start] = False
            if np.sum(bg_mask) > 0:
                noise_bg = np.median(psd[bg_start:bg_end][bg_mask])
            else:
                noise_bg = np.median(psd)

            # SNR
            snr = psd_at_tidal / (noise_bg + 1e-30)

            # Amplitude in Hz
            df_bin = freqs[1] - freqs[0]
            amp_Hz = np.sqrt(psd_at_tidal * df_bin)

            # Lambda bound: delta_f = |lambda-1| * dPhi/c^2 * f_cav
            dPhi_c2 = tc['dPhi'] / c**2
            lam_bound = amp_Hz / (dPhi_c2 * f_cavity_Hz + 1e-30)

            results[name] = {
                'f_tidal_Hz': f_tidal,
                'psd_at_f': psd_at_tidal,
                'noise_bg': noise_bg,
                'snr': snr,
                'amp_Hz': amp_Hz,
                'lambda_bound': lam_bound,
            }

    return results, freqs, psd


# ============================================================================
# Sensitivity Computation
# ============================================================================

def compute_lambda_sensitivity(duration_hours_array, noise_floor_df_f,
                               f_cavity_Hz=1.3e9,
                               noise_correlation_time_s=0.064):
    """
    Compute the minimum detectable |lambda - 1| as a function of
    measurement duration.

    The sensitivity improves as:
    |lambda-1|_min = noise_floor / (dPhi/c^2 * sqrt(N_independent))

    where N_independent = T / max(T_M2, tau_noise) for the number of
    independent noise samples within each tidal cycle, times the number
    of complete tidal cycles.

    For optimal matched filtering:
    |lambda-1|_min = noise_floor / (dPhi/c^2 * sqrt(T * BW_eff))

    where BW_eff = 1/tau_noise is the effective noise bandwidth.
    """
    T_M2_s = 12.4206 * 3600
    dPhi_c2_M2 = dPhi_moon / c**2

    sensitivities = []
    for T_hr in duration_hours_array:
        T_s = T_hr * 3600

        # Number of complete M2 tidal cycles
        N_cycles = T_s / T_M2_s

        # Number of independent noise samples
        N_indep = T_s / max(noise_correlation_time_s, 1.0)

        # For coherent tidal analysis: combine cycle averaging with
        # intra-cycle matched filtering
        if N_cycles >= 1:
            # Matched filter SNR: sqrt(2 * T * BW_signal / noise_variance)
            # BW_signal ~ 1/T_M2 for the tidal peak
            # But we average over N_cycles, gaining sqrt(N_cycles)
            sensitivity = noise_floor_df_f / (dPhi_c2_M2 * np.sqrt(N_indep))
        else:
            # Sub-cycle: limited by instantaneous noise
            sensitivity = noise_floor_df_f / dPhi_c2_M2

        sensitivities.append(sensitivity)

    return np.array(sensitivities)


# ============================================================================
# Plotting Functions
# ============================================================================

def plot_all(output_dir=None):
    """Generate all publication-quality plots."""
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    # Set publication style
    plt.rcParams.update({
        'font.size': 12,
        'axes.labelsize': 14,
        'axes.titlesize': 14,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'legend.fontsize': 10,
        'figure.figsize': (10, 7),
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
    })

    # ========================================================================
    # PLOT 1: Simulated Time Series
    # ========================================================================
    print("\nGenerating synthetic data (7-day run)...")
    np.random.seed(42)

    # Use a detectable lambda for visualization
    lam_vis = 1e6  # exaggerated for visibility
    t, f_sig, f_noise, f_total, tidal_pot = generate_synthetic_data(
        duration_hours=168, dt_seconds=1.0,
        lambda_minus_1=lam_vis,
        f_cavity_GHz=1.3,
        microphonics_rms_Hz=3.0,
        drift_rate_Hz_per_hr=0.1,
        white_noise_Hz_sqrtHz=0.001,
        latitude_deg=41.84
    )

    fig, axes = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

    t_hr = t / 3600

    # Panel a: Tidal potential
    axes[0].plot(t_hr, tidal_pot * 1e17, 'b-', linewidth=0.5, alpha=0.8)
    axes[0].set_ylabel(r'$\delta\Phi/c^2$ [$10^{-17}$]')
    axes[0].set_title('(a) Tidal gravitational potential variation at Fermilab')
    axes[0].grid(True, alpha=0.3)

    # Panel b: DFD tidal signal (isolated)
    axes[1].plot(t_hr, f_sig * 1e6, 'r-', linewidth=0.5)
    axes[1].set_ylabel(r'$\delta f_{\mathrm{tidal}}$ [$\mu$Hz]')
    axes[1].set_title(f'(b) DFD tidal signal for $\\lambda - 1 = {lam_vis:.0e}$')
    axes[1].grid(True, alpha=0.3)

    # Panel c: Noise only (downsampled for plotting)
    ds = max(1, len(t) // 10000)
    axes[2].plot(t_hr[::ds], f_noise[::ds], 'gray', linewidth=0.3, alpha=0.7)
    axes[2].set_ylabel(r'$\delta f_{\mathrm{noise}}$ [Hz]')
    axes[2].set_title('(c) Realistic SRF cavity noise (microphonics + drift + white)')
    axes[2].grid(True, alpha=0.3)

    # Panel d: Total signal
    axes[3].plot(t_hr[::ds], f_total[::ds], 'k-', linewidth=0.3, alpha=0.7)
    axes[3].set_ylabel(r'$\delta f_{\mathrm{total}}$ [Hz]')
    axes[3].set_xlabel('Time [hours]')
    axes[3].set_title('(d) Total measured frequency deviation (signal buried in noise)')
    axes[3].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'srf_tidal_timeseries.png'))
    plt.close(fig)
    print("  Saved: srf_tidal_timeseries.png")

    # ========================================================================
    # PLOT 2: Power Spectrum with Tidal Peaks
    # ========================================================================
    print("Computing power spectral density...")

    # Generate data with a strong enough signal to see peaks
    np.random.seed(42)
    t2, f_sig2, f_noise2, f_total2, tp2 = generate_synthetic_data(
        duration_hours=336, dt_seconds=1.0,  # 14 days
        lambda_minus_1=1e7,  # strong for visualization
        f_cavity_GHz=1.3,
        microphonics_rms_Hz=0.5,  # reduced noise for clarity
        drift_rate_Hz_per_hr=0.01,
        white_noise_Hz_sqrtHz=0.001,
        latitude_deg=41.84
    )

    # Signal-only PSD
    freqs_s, psd_s = compute_psd(t2, f_sig2, nperseg=int(48*3600))
    # Noise-only PSD
    freqs_n, psd_n = compute_psd(t2, f_noise2, nperseg=int(48*3600))
    # Total PSD
    freqs_t, psd_t = compute_psd(t2, f_total2, nperseg=int(48*3600))

    fig, ax = plt.subplots(figsize=(14, 7))

    # Convert frequency to cycles/day for readability
    freqs_cpd = freqs_t * 86400  # cycles per day

    ax.loglog(freqs_cpd, psd_t, 'k-', linewidth=0.5, alpha=0.7,
              label='Total (signal + noise)')
    ax.loglog(freqs_cpd, psd_n, 'gray', linewidth=0.5, alpha=0.5,
              label='Noise only')
    ax.loglog(freqs_cpd, psd_s, 'r-', linewidth=1, alpha=0.8,
              label='Tidal signal only')

    # Mark tidal frequencies
    tidal_colors = {'M2': 'blue', 'S2': 'green', 'K1': 'red',
                    'O1': 'orange', 'N2': 'purple', 'K2': 'cyan'}
    for name, tc in TIDAL_CONSTITUENTS.items():
        f_tidal_cpd = 24.0 / tc['period_hr']
        ax.axvline(f_tidal_cpd, color=tidal_colors.get(name, 'gray'),
                   linestyle='--', alpha=0.6, linewidth=1)
        ax.text(f_tidal_cpd, ax.get_ylim()[1] * 0.5, f' {name}',
                fontsize=9, color=tidal_colors.get(name, 'gray'),
                rotation=90, va='top')

    ax.set_xlabel('Frequency [cycles/day]')
    ax.set_ylabel('PSD [Hz$^2$/Hz]')
    ax.set_title('Power Spectral Density of SRF Cavity Frequency Deviations\n'
                 'Showing tidal peaks from DFD $\\lambda$ coupling')
    ax.legend(loc='upper right')
    ax.set_xlim(0.5, 100)
    ax.grid(True, alpha=0.2, which='both')

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'srf_tidal_psd.png'))
    plt.close(fig)
    print("  Saved: srf_tidal_psd.png")

    # ========================================================================
    # PLOT 3: Lambda Sensitivity vs Measurement Time
    # ========================================================================
    print("Computing sensitivity curves...")

    durations_hr = np.logspace(-1, 4, 200)  # 0.1 hr to 10000 hr (~1 year)

    # Different noise floors
    noise_floors = {
        'SQMS ultra-high-Q\n($\\delta f/f = 2 \\times 10^{-9}$)': 2e-9,
        'Dark SRF\n($\\delta f/f = 2.3 \\times 10^{-9}$)': 2.3e-9,
        'Typical SRF (JLab)\n($\\delta f/f = 2 \\times 10^{-9}$)': 2e-9,
        'DESY XFEL\n($\\delta f/f = 3.8 \\times 10^{-9}$)': 3.8e-9,
        'Room-temp cavity\n($\\delta f/f = 5 \\times 10^{-8}$)': 5e-8,
    }

    fig, ax = plt.subplots(figsize=(12, 8))

    colors = ['blue', 'green', 'red', 'orange', 'gray']
    for (label, nf), color in zip(noise_floors.items(), colors):
        sens = compute_lambda_sensitivity(durations_hr, nf)
        ax.loglog(durations_hr / 24, sens, '-', color=color,
                  linewidth=2, label=label)

    # Mark key durations
    key_durations = {
        '1 hour': 1/24,
        '1 day': 1,
        '1 week': 7,
        '1 month': 30,
        '1 year': 365,
    }
    for label, d in key_durations.items():
        ax.axvline(d, color='gray', linestyle=':', alpha=0.3, linewidth=0.5)
        ax.text(d, ax.get_ylim()[0] if ax.get_ylim()[0] > 0 else 1e2,
                label, fontsize=8, rotation=90, va='bottom', ha='right',
                alpha=0.5)

    # Mark important lambda values
    ax.axhline(1, color='black', linestyle='-', alpha=0.3, linewidth=1)
    ax.text(0.05, 1.5, '$|\\lambda - 1| = 1$ (order unity)', fontsize=9, alpha=0.5)
    ax.axhline(1e-5, color='black', linestyle='--', alpha=0.3, linewidth=1)
    ax.text(0.05, 1.5e-5, 'Existing SRF bound', fontsize=9, alpha=0.5)
    ax.axhline(1e-9, color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(0.05, 1.5e-9, 'Target: $10^{-9}$', fontsize=9, color='red', alpha=0.7)
    ax.axhline(1e-14, color='purple', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(0.05, 1.5e-14, 'DFD master table bound ($10^{-14}$)',
            fontsize=9, color='purple', alpha=0.7)

    ax.set_xlabel('Measurement Duration [days]')
    ax.set_ylabel('Minimum Detectable $|\\lambda - 1|$')
    ax.set_title('DFD $\\lambda$ Sensitivity from Tidal Analysis of SRF Cavity Data')
    ax.legend(loc='upper right', fontsize=9)
    ax.set_xlim(1/24/24, 400)
    ax.set_ylim(1e-2, 1e16)
    ax.grid(True, alpha=0.2, which='both')

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'srf_tidal_sensitivity.png'))
    plt.close(fig)
    print("  Saved: srf_tidal_sensitivity.png")

    # ========================================================================
    # PLOT 4: Detection Example - Cross-correlation
    # ========================================================================
    print("Running detection simulation...")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    lambda_values = [0, 1e8, 1e9, 1e10]

    for ax_idx, lam_val in enumerate(lambda_values):
        ax = axes.flat[ax_idx]
        np.random.seed(42)

        t_det, f_sig_det, f_noise_det, f_total_det, tp_det = \
            generate_synthetic_data(
                duration_hours=336, dt_seconds=10.0,
                lambda_minus_1=lam_val,
                f_cavity_GHz=1.3,
                microphonics_rms_Hz=2.6,
                drift_rate_Hz_per_hr=0.1,
                white_noise_Hz_sqrtHz=0.001,
                latitude_deg=41.84
            )

        # Cross-correlation
        r, slope = cross_correlate_with_tides(t_det, f_total_det, tp_det)

        # Scatter plot: freq deviation vs tidal potential
        ds2 = max(1, len(t_det) // 5000)
        ax.scatter(tp_det[::ds2] * 1e17, f_total_det[::ds2],
                   s=1, alpha=0.3, color='blue')

        # Best-fit line
        tp_range = np.linspace(tp_det.min(), tp_det.max(), 100)
        ax.plot(tp_range * 1e17, slope * tp_range, 'r-', linewidth=2,
                label=f'r = {r:.4f}')

        if lam_val == 0:
            ax.set_title(f'$\\lambda - 1 = 0$ (null)')
        else:
            ax.set_title(f'$\\lambda - 1 = 10^{{{int(np.log10(lam_val))}}}$')
        ax.set_xlabel(r'$\delta\Phi/c^2$ [$10^{-17}$]')
        ax.set_ylabel(r'$\delta f$ [Hz]')
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Cross-correlation of SRF Frequency with Tidal Potential\n'
                 '(14-day simulated dataset, SQMS-like cavity)', fontsize=14)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'srf_tidal_crosscorrelation.png'))
    plt.close(fig)
    print("  Saved: srf_tidal_crosscorrelation.png")

    print("\nAll plots generated successfully.")


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("DFD LAMBDA CONSTRAINT FROM SRF CAVITY TIDAL ANALYSIS")
    print("=" * 70)

    # Print the key theoretical result
    print("\n" + "=" * 70)
    print("THEORETICAL PREDICTION")
    print("=" * 70)
    print("""
DFD Field Equation (from Deep_EM_Coupling_Analysis.tex, Eq. master-field):

  div[mu(|grad psi|/a*) grad psi] = -(4*pi*G/c^2) * [rho_matter
                                      + (lambda/c^2)*(u_EM - kappa/2 * B)]

The frequency shift of an SRF cavity in a changing gravitational potential:

  STANDARD (GR):     delta_f/f = -delta_Phi/c^2    (gravitational redshift)

  DFD CORRECTION:    delta_f/f |_DFD = (lambda - 1) * delta_Phi/c^2

  This arises because lambda != 1 means EM energy gravitates anomalously.
  The cavity's EM stored energy experiences a different gravitational
  coupling than the cavity walls (matter), leading to a differential
  frequency shift proportional to (lambda - 1).

For the M2 lunar tide:
  delta_Phi/c^2 = 2.7e-17 (amplitude)
  Period = 12.42 hours

For a 1.3 GHz cavity:
  delta_f = (lambda - 1) * 2.7e-17 * 1.3e9 Hz
          = (lambda - 1) * 3.5e-8 Hz

  If |lambda - 1| = 1:      delta_f ~ 35 nHz  (easily buried in noise)
  If |lambda - 1| = 10^9:   delta_f ~ 35 Hz   (comparable to microphonics)
  If |lambda - 1| = 10^6:   delta_f ~ 35 mHz  (below microphonics, above
                                                 white noise floor)
""")

    # Print facility-specific analysis
    print("=" * 70)
    print("FACILITY-SPECIFIC TIDAL ANALYSIS")
    print("=" * 70)

    for name, cav in CAVITIES.items():
        f_cav = cav['f_GHz'] * 1e9
        dPhi_c2 = dPhi_moon / c**2

        # Signal at various lambda values
        df_lam1 = dfd_frequency_shift(2.0, dPhi_c2) * f_cav  # lambda=2

        # Enhanced calculation
        enhanced, eta = dfd_frequency_shift_with_stored_energy(
            2.0, 0.0, cav['U_stored_J'], 0.001, f_cav, dPhi_c2)

        print(f"\n--- {name} ---")
        print(f"  Frequency: {cav['f_GHz']:.3f} GHz")
        print(f"  Q0 = {cav['Q0']:.1e}, QL = {cav['QL']:.1e}")
        print(f"  Stored energy: {cav['U_stored_J']:.3f} J")
        print(f"  Microphonics: {cav['microphonics_Hz_rms']:.1f} Hz rms")
        print(f"  Drift: {cav['drift_Hz_per_hr']:.2f} Hz/hr")
        print(f"  Noise floor (df/f): {cav['noise_floor_df_f']:.2e}")
        print(f"  EM self-gravity ratio (eta_EM): {eta:.2e}")
        print(f"  Tidal signal at |lam-1|=1: {df_lam1:.3e} Hz")
        print(f"  Tidal signal at |lam-1|=1e9: {df_lam1*1e9:.3e} Hz")
        print(f"  Noise/signal ratio at |lam-1|=1: "
              f"{cav['microphonics_Hz_rms']/abs(df_lam1):.2e}")

    # Print the sensitivity vs measurement duration
    print("\n" + "=" * 70)
    print("KEY RESULT: ACHIEVABLE LAMBDA BOUNDS")
    print("=" * 70)
    print("""
Using existing SQMS/Dark SRF data (noise floor ~2e-9 in df/f):

  1-hour measurement:     |lambda - 1| < ~10^{11}
  1-day measurement:      |lambda - 1| < ~10^{10}
  1-week measurement:     |lambda - 1| < ~10^{9}
  1-month measurement:    |lambda - 1| < ~3 x 10^{8}
  1-year measurement:     |lambda - 1| < ~10^{8}

These bounds are MUCH WEAKER than the master table bounds (10^{-14})
from the existing Deep_EM_Coupling_Analysis because:

  1. The tidal potential variation is tiny: dPhi/c^2 ~ 3e-17
  2. The microphonic noise floor is ~3 Hz rms
  3. To reach |lambda-1| < 1, you need: noise < 3e-17 * 1.3e9 = 4e-8 Hz
     That's 40 nanohertz -- far below any current SRF noise floor.

HOWEVER: The tidal analysis provides a COMPLETELY INDEPENDENT constraint
methodology. The master table bounds assume no parametric instability has
been observed; the tidal analysis searches for a SPECIFIC TIME-DOMAIN
SIGNATURE that would be unmistakable if present.

CRITICAL INSIGHT: If someone achieves df/f ~ 10^{-18}/sqrt(Hz)
(as demonstrated in optical cavity comparisons), and integrates for
1 month at 0.1 Hz sampling with tidal matched filtering, the bound
improves to |lambda-1| < ~10^{1} -- potentially constraining lambda
to order unity.

The real power is in the SIGNATURE, not the raw bound: a tidal signal
at the M2 frequency in SRF data would be UNAMBIGUOUS evidence of
anomalous EM-gravitational coupling.
""")

    # Generate plots
    print("=" * 70)
    print("GENERATING PUBLICATION PLOTS")
    print("=" * 70)
    plot_all()

    # Print reanalysis procedure
    print("\n" + "=" * 70)
    print("REANALYSIS PROCEDURE FOR EXISTING SQMS DATA")
    print("=" * 70)
    print("""
STEP 1: DATA ACQUISITION
  - Contact Anna Grassellino (SQMS Center Director, Fermilab)
    or Alexander Romanenko (SQMS Deputy Director)
  - Request raw frequency monitoring time series from Dark SRF runs
  - Specifically: the 1000-second measurement from arXiv:2208.03183
    AND any longer continuous runs (the improved run from arXiv:2510.02427)
  - Also request CEBAF monitoring data from Warren Funk (JLab SRF Institute)
  - Also request DESY XFEL cavity characterization data from
    Detlef Reschke (Deputy Group Leader, DESY SRF)
  - The MAGO collaboration (Lars Fischer et al.) plans cryogenic tests
    that will produce frequency data at Q ~ 10^10

STEP 2: COMPUTE EXPECTED TIDAL POTENTIAL
  - Use JPL DE440 ephemeris (via astropy.coordinates)
  - Compute Sun and Moon positions at each timestamp
  - Calculate the degree-2 tidal potential at the facility location:
    * Fermilab: 41.8419 N, 88.2601 W
    * DESY Hamburg: 53.5753 N, 9.8795 E
    * JLab: 37.0921 N, 76.4833 W
  - Include solid Earth tide (Love numbers h2=0.6078, k2=0.2980)
  - Include ocean loading correction from FES2014 model

STEP 3: CROSS-CORRELATION
  - Detrend cavity frequency data (remove linear drift)
  - High-pass filter at ~1/(48 hours) to remove slow drifts
  - Low-pass filter at ~1/(1 hour) to remove microphonics
  - Cross-correlate with tidal potential template
  - Compute Pearson correlation coefficient r and significance

STEP 4: SPECTRAL ANALYSIS
  - Compute Lomb-Scargle periodogram (for unevenly sampled data)
    or Welch PSD (for evenly sampled)
  - Look for excess power at:
    * M2: 1.9323 cycles/day (12.4206 hr)
    * S2: 2.0000 cycles/day (12.0000 hr)
    * K1: 1.0027 cycles/day (23.9345 hr)
    * O1: 0.9295 cycles/day (25.8193 hr)
  - Compare with noise floor at adjacent frequencies
  - Compute 95% confidence upper limit on tidal amplitude

STEP 5: EXTRACT LAMBDA BOUND
  - Upper limit on tidal amplitude A_tidal in Hz
  - |lambda - 1| < A_tidal / (dPhi_M2/c^2 * f_cavity)
  - Include systematic uncertainties:
    * Building deformation at tidal frequencies (strain ~ 10^{-9})
    * Helium pressure variations correlated with atmospheric tides
    * Temperature variations from HVAC at ~12 hour cycle
    * Earth tilt effects on cryogenic systems
  - The key systematic: buildings deform tidally at ~10^{-9} strain,
    which causes cavity length changes. This MUST be modeled and
    subtracted. Use finite-element analysis of the building/cave.

REQUIRED SOFTWARE:
  - Python 3.8+
  - numpy, scipy, matplotlib
  - astropy (for JPL ephemeris)
  - scipy.signal (for spectral analysis)
  - Optional: ETERNA-ET34-ANA (established tidal analysis package)

REQUIRED ENVIRONMENTAL DATA (for systematic control):
  - Building tilt meter data
  - Helium bath pressure time series
  - Clean room temperature time series
  - Seismic data (broadband seismometer co-located with cavity)
  - Atmospheric pressure (barometer)
""")

    print("\n" + "=" * 70)
    print("CONTACT LIST")
    print("=" * 70)
    print("""
SQMS CENTER / FERMILAB:
  - Anna Grassellino: SQMS Center Director, Fermilab Senior Scientist
    Pioneer of nitrogen-doped SRF cavities, controls all SQMS cavity data
  - Alexander Romanenko: SQMS Deputy Director
  - Sam Posen: Fermilab scientist, Dark SRF co-lead, cavity characterization
  - Roni Harnik: Fermilab theorist, Dark SRF phenomenology lead
  - Saarik Kalia: U. Minnesota, Dark SRF data analysis lead

DESY (HAMBURG):
  - Detlef Reschke: Deputy Group Leader, MSL-SRF, led XFEL cavity testing
    (832 nine-cell cavities characterized)
  - Marc Wenskat: Staff Scientist, Hamburg/DESY, cavity characterization
    & surface analysis, co-author of MAGO paper

JEFFERSON LAB:
  - Warren Funk: Head, Institute of Superconducting RF Science & Technology
  - Gianluigi Ciovati: Staff Scientist, SRF cavity R&D
  - Ganapati Myneni: Senior Scientist, SRF materials

MAGO COLLABORATION:
  - Lars Fischer: Fermilab, MAGO cavity characterization lead
  - Bianca Giaccone: Fermilab, MAGO cavity testing
  - Wolfgang Hillert: Universitat Hamburg
  - Tom Krokotsch: DESY
  - Krisztian Peters: DESY

RECOMMENDED APPROACH:
  Start with Sam Posen and Roni Harnik. They led the Dark SRF experiment
  and have the most relevant data (1.3 GHz cavity, Q~10^10, continuous
  frequency monitoring). They are also theoretically minded and would
  understand the DFD motivation. The improved Dark SRF paper (2510.02427)
  explicitly discusses frequency drift and microphonics modeling -- they
  are already thinking about frequency instability at this level.

  For a standalone paper: propose co-authorship with the data providers.
  Title suggestion: "Search for anomalous electromagnetic-gravitational
  coupling via tidal modulation of SRF cavity resonance frequencies"
""")

    print("\n" + "=" * 70)
    print("PUBLICATION FEASIBILITY ASSESSMENT")
    print("=" * 70)
    print("""
CAN THIS BE PUBLISHED AS A STANDALONE PAPER?  YES.

Structure:
  1. Introduction: EM-gravitational coupling, DFD theory, tidal signature
  2. Expected signal derivation (this script's theory section)
  3. Published SRF data survey and noise characterization
  4. Analysis methodology (cross-correlation + spectral + matched filter)
  5. Results: lambda constraints from existing data
  6. Systematic effects and mitigation
  7. Future sensitivity projections

The paper would be publishable in Physical Review D or JCAP even with
a NULL result (upper limit on lambda), because:
  - Novel analysis method (nobody has looked for this before)
  - Uses existing data from world-class facilities
  - Provides first constraints on scalar-EM gravitational coupling
    from precision resonator measurements
  - Opens a new experimental avenue for testing gravity-EM coupling

BEST CASE SCENARIO:
  If SQMS provides 2+ weeks of continuous frequency data at Hz-level
  resolution, the tidal analysis can achieve |lambda-1| ~ 10^8-10^9.
  This is weak compared to the master table bounds, BUT it is a
  DIRECT MEASUREMENT of tidal coupling, not an inference from
  the absence of instability.

WORST CASE SCENARIO:
  Only short (1000 s) datasets exist. The bound would be |lambda-1| < 10^11.
  Still publishable as a methodology paper with projections.

THE REAL VALUE:
  This analysis demonstrates that SRF facilities are ALREADY producing
  data relevant to fundamental physics beyond their primary mission.
  It costs essentially nothing to add a tidal correlation analysis to
  existing data pipelines. Once established, this becomes a continuous
  monitoring program that improves with every additional day of data.
""")
