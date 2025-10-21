
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from dfd_model import DFDInputs, compute_correction
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="DFD GPS Correction API", version="0.1.0",
              description="Density Field Dynamics web API for ψ-based GPS timing/range correction.")

class CorrectionRequest(BaseModel):
    lat: float = Field(..., description="Latitude in degrees")
    lon: float = Field(..., description="Longitude in degrees")
    h_m: float = Field(..., description="Ellipsoidal height in meters")
    temp_K: float = Field(..., description="Local air temperature (Kelvin)")
    pressure_Pa: float = Field(..., description="Surface pressure (Pa)")
    rh_frac: float = Field(0.5, description="Relative humidity (0..1)")
    elev_deg: float = Field(45.0, description="Satellite elevation (deg)")
    range_m: float = Field(..., description="Nominal geometric range (m)")

class CorrectionResponse(BaseModel):
    psi_surface: float
    delta_phi_over_c2: float
    one_way_delay_s: float
    range_bias_m: float
    timing_bias_ns: float
    corrected_range_m: float
    quality_flag: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/dfd-correct", response_model=CorrectionResponse)
def dfd_correct(payload: CorrectionRequest):
    out = compute_correction(DFDInputs(**payload.model_dump()))
    return CorrectionResponse(**out.__dict__)

# Serve static demo at root
app.mount("/", StaticFiles(directory="static", html=True), name="static")
