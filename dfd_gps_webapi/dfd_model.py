
import math
from dataclasses import dataclass

# Constants
C = 299_792_458.0              # m/s
G0 = 9.80665                   # m/s^2 standard gravity
C2 = C*C
# Simple standard atmosphere baseline (troposphere, sea level)
P0 = 101325.0                  # Pa
T0 = 288.15                    # K
L  = 0.0065                    # K/m lapse rate
R  = 8.314462618               # J/(mol K)
M  = 0.0289644                 # kg/mol
RH_DEFAULT = 0.5

@dataclass
class DFDInputs:
    lat: float       # degrees
    lon: float       # degrees
    h_m: float       # ellipsoidal height (m)
    temp_K: float    # local air temperature (K)
    pressure_Pa: float  # local surface pressure (Pa)
    rh_frac: float   # relative humidity (0..1)
    elev_deg: float  # satellite elevation angle (deg)
    range_m: float   # nominal geometric range (m)

@dataclass
class DFDOutputs:
    psi_surface: float
    delta_phi_over_c2: float
    one_way_delay_s: float
    range_bias_m: float
    timing_bias_ns: float
    corrected_range_m: float
    quality_flag: str

def barometric_pressure(h_m: float, T_sea_K: float = T0) -> float:
    """
    International Standard Atmosphere (ISA) barometric formula up to ~11 km.
    """
    return P0 * (1 - (L * h_m) / T_sea_K) ** (G0 * M / (R * L))

def saturation_vapor_pressure_Pa(T_K: float) -> float:
    """
    Tetens approximation (Pa).
    """
    T_C = T_K - 273.15
    return 610.94 * math.exp((17.625 * T_C) / (T_C + 243.04))

def refractivity_components(pressure_Pa: float, temp_K: float, rh_frac: float):
    """
    Simple Smith–Weintraub refractivity split into dry and wet parts:
    N ≈ k1*(P/T) + k2'*(e/T^2), with k1≈77.6 K/mb, k2'≈3.73e5 K^2/mb.
    Returns Ndry, Nwet (N-units).
    """
    # Convert to mb (hPa)
    P_hPa = pressure_Pa / 100.0
    e_Pa = saturation_vapor_pressure_Pa(temp_K) * max(0.0, min(1.0, rh_frac))
    e_hPa = e_Pa / 100.0

    k1 = 77.6
    k2p = 3.73e5
    Ndry = k1 * (P_hPa / temp_K)
    Nwet = k2p * (e_hPa / (temp_K * temp_K))
    return Ndry, Nwet

def zenith_tropo_delay_m(pressure_Pa: float, temp_K: float, rh_frac: float) -> float:
    """
    Very lightweight Saastamoinen-like zenith total delay (dry + wet) in meters.
    This is a conventional meteorology formula used here as a *proxy* for ψ-driven
    refractive delay through the atmospheric column.
    """
    Nd, Nw = refractivity_components(pressure_Pa, temp_K, rh_frac)
    P_hPa = pressure_Pa / 100.0
    e_Pa = saturation_vapor_pressure_Pa(temp_K) * max(0.0, min(1.0, rh_frac))
    e_hPa = e_Pa / 100.0
    ZHD = 0.0022768 * P_hPa * (1.0)  # hydrostatic meters
    ZWD = 0.002277 * (1255.0 / temp_K + 0.05) * e_hPa
    return ZHD + ZWD

def elevation_mapping(elev_deg: float) -> float:
    """
    Simple Niell-like mapping: m(e) ~ 1/sin(e + 0.1°) to avoid singularity at low e.
    """
    e_deg = max(0.1, min(89.9, elev_deg))
    e_rad = math.radians(e_deg)
    return 1.0 / math.sin(e_rad + math.radians(0.1))

def psi_from_potential(h_m: float):
    """
    ψ ≈ 2Φ/c^2 with Φ ≈ g0 * h (relative to sea level). Returns (psi, ΔΦ/c^2).
    """
    dphi_over_c2 = (G0 * h_m) / (C2)
    psi = -2.0 * dphi_over_c2
    return psi, dphi_over_c2

def compute_correction(inp: DFDInputs) -> DFDOutputs:
    psi_surf, dphi_over_c2 = psi_from_potential(inp.h_m)

    # Zenith-equivalent atmospheric delay (meters)
    ztd_m = zenith_tropo_delay_m(
        pressure_Pa=inp.pressure_Pa,
        temp_K=inp.temp_K,
        rh_frac=inp.rh_frac if inp.rh_frac is not None else 0.5
    )
    # LOS mapping
    m_elev = elevation_mapping(inp.elev_deg if inp.elev_deg is not None else 45.0)
    los_delay_m = ztd_m * m_elev

    timing_bias_s = los_delay_m / C
    corrected_range = max(0.0, inp.range_m - los_delay_m)

    return DFDOutputs(
        psi_surface=psi_surf,
        delta_phi_over_c2=dphi_over_c2,
        one_way_delay_s=timing_bias_s,
        range_bias_m=los_delay_m,
        timing_bias_ns=timing_bias_s * 1e9,
        corrected_range_m=corrected_range,
        quality_flag="ψ from Φ≈g*h; delay uses met-driven refractivity as ψ-proxy; simple elevation mapping."
    )
