
# DFD GPS Correction Web API & Demo

A minimal scaffold to deploy a DFD-based GPS correction API and static demo at **densityfielddynamics.com**.

## Features
- `/dfd-correct` endpoint (FastAPI) computes ψ estimate and atmospheric (refractivity) delay, maps to line-of-sight, returns range/timing corrections.
- Static demo UI at `/` that POSTs to the API.
- Synthetic **benchmark** showing RMSE reduction when applying the correction.

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
# open http://127.0.0.1:8000 (demo) and /docs (Swagger)
```

## Docker
```bash
docker build -t dfd-gps-api .
docker run -p 8000:8000 dfd-gps-api
```

## Benchmark
```bash
python benchmark_demo.py
```
Outputs:
- `benchmark_error_hist.png`
- `benchmark_results.csv`
- `benchmark_summary.json`
