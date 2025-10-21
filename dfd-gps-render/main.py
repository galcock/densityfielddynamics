# main.py
import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# ---------- DFD model (lightweight, no heavy deps) ----------
C = 299_792_458.0        # m/s
G0 = 9.80665             # m/s^2  (near-surface)
# ψ ≈ -2ΔΦ/c^2 with ΔΦ ≈ g * h (relative to sea level)

def saturation_vapor_pressure_Pa(T_K: float) -> float:
    """Tetens approximation for water vapor saturation pressure (Pa)."""
    T_C = T_K - 273.15
    return 610.94 * math.exp((17.625 * T_C) / (T_C + 243.04))

def zenith_tropo_delay_m(pressure_Pa: float, temp_K: float, rh_frac: float) -> float:
    """Very small Saastamoinen-like estimate of zenith delay (meters)."""
    P_hPa = pressure_Pa / 100.0
    e_hPa = saturation_vapor_pressure_Pa(temp_K) * max(0.0, min(1.0, rh_frac)) / 100.0
    ZHD = 0.0022768 * P_hPa
    ZWD = 0.002277 * (1255.0 / temp_K + 0.05) * e_hPa
    return ZHD + ZWD

def elevation_mapping(elev_deg: float) -> float:
    """Simple mapping m(e) ≈ 1/sin(e + 0.1°) to avoid blow-up near horizon."""
    e_rad = math.radians(max(0.1, min(89.9, elev_deg)))
    return 1.0 / math.sin(e_rad + math.radians(0.1))

# ---------- FastAPI models ----------
class CorrectionRequest(BaseModel):
    lat: float = Field(..., description="Latitude in degrees")
    lon: float = Field(..., description="Longitude in degrees")
    h_m: float = Field(..., description="Ellipsoidal height (m)")
    temp_K: float = Field(..., description="Temperature (K)")
    pressure_Pa: float = Field(..., description="Surface pressure (Pa)")
    rh_frac: float = Field(0.5, description="Relative humidity 0..1")
    elev_deg: float = Field(45.0, description="Satellite elevation angle (deg)")
    range_m: float = Field(..., description="Nominal geometric range (m)")

class CorrectionResponse(BaseModel):
    psi_surface: float
    delta_phi_over_c2: float
    one_way_delay_s: float
    range_bias_m: float
    timing_bias_ns: float
    corrected_range_m: float
    quality_flag: str

# ---------- App ----------
app = FastAPI(title="DFD GPS Correction API (Render)")

# CORS (allow your Vercel site + direct access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://densityfielddynamics.com",
        "https://www.densityfielddynamics.com",
        "*",  # you can remove "*" later if you want to lock it down
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/dfd-correct", response_model=CorrectionResponse)
def dfd_correct(payload: CorrectionRequest):
    # ψ and ΔΦ/c^2 from height
    dphi_over_c2 = (G0 * payload.h_m) / (C * C)
    psi_surface = -2.0 * dphi_over_c2

    # Atmospheric refractivity delay as ψ-proxy
    ztd_m = zenith_tropo_delay_m(payload.pressure_Pa, payload.temp_K, payload.rh_frac)
    los_delay_m = ztd_m * elevation_mapping(payload.elev_deg)

    timing_bias_s = los_delay_m / C
    corrected_range = max(0.0, payload.range_m - los_delay_m)

    return CorrectionResponse(
        psi_surface=psi_surface,
        delta_phi_over_c2=dphi_over_c2,
        one_way_delay_s=timing_bias_s,
        range_bias_m=los_delay_m,
        timing_bias_ns=timing_bias_s * 1e9,
        corrected_range_m=corrected_range,
        quality_flag="ψ from Φ≈g*h; refractivity proxy for delay; simple elevation mapping."
    )

# Serve the demo UI at "/"
app.mount("/", StaticFiles(directory="static", html=True), name="static")
