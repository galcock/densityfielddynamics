# /api/index.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import math

# ---- DFD model bits (trimmed from our scaffold) ----
C = 299_792_458.0
G0 = 9.80665

def saturation_vapor_pressure_Pa(T_K: float) -> float:
    T_C = T_K - 273.15
    return 610.94 * math.exp((17.625 * T_C) / (T_C + 243.04))

def zenith_tropo_delay_m(pressure_Pa: float, temp_K: float, rh_frac: float) -> float:
    P_hPa = pressure_Pa / 100.0
    e_hPa = saturation_vapor_pressure_Pa(temp_K) * max(0.0, min(1.0, rh_frac)) / 100.0
    ZHD = 0.0022768 * P_hPa
    ZWD = 0.002277 * (1255.0 / temp_K + 0.05) * e_hPa
    return ZHD + ZWD

def elevation_mapping(elev_deg: float) -> float:
    e_rad = math.radians(max(0.1, min(89.9, elev_deg)))
    return 1.0 / math.sin(e_rad + math.radians(0.1))

class CorrectionRequest(BaseModel):
    lat: float
    lon: float
    h_m: float
    temp_K: float
    pressure_Pa: float
    rh_frac: float = 0.5
    elev_deg: float = 45.0
    range_m: float

class CorrectionResponse(BaseModel):
    psi_surface: float
    delta_phi_over_c2: float
    one_way_delay_s: float
    range_bias_m: float
    timing_bias_ns: float
    corrected_range_m: float
    quality_flag: str

app = FastAPI(title="DFD GPS Correction (Vercel)")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/dfd-correct", response_model=CorrectionResponse)
def dfd_correct(payload: CorrectionRequest):
    dphi_over_c2 = (G0 * payload.h_m) / (C*C)
    psi_surf = -2.0 * dphi_over_c2

    ztd = zenith_tropo_delay_m(payload.pressure_Pa, payload.temp_K, payload.rh_frac)
    m_e = elevation_mapping(payload.elev_deg)
    los_delay_m = ztd * m_e

    timing_bias_s = los_delay_m / C
    corrected_range = max(0.0, payload.range_m - los_delay_m)

    return CorrectionResponse(
        psi_surface=psi_surf,
        delta_phi_over_c2=dphi_over_c2,
        one_way_delay_s=timing_bias_s,
        range_bias_m=los_delay_m,
        timing_bias_ns=timing_bias_s * 1e9,
        corrected_range_m=corrected_range,
        quality_flag="Vercel serverless FastAPI; ψ from Φ≈g*h; refractivity proxy for delay."
    )
