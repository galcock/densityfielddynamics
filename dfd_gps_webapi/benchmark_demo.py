
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dfd_model import compute_correction, DFDInputs

np.random.seed(42)

N = 500
lat = 34.05
lon = -118.25
h_m = 100.0
true_range_m = 20_200_000.0

temps = np.random.normal(293.15, 4.0, N)
press = np.random.normal(101325.0, 1200.0, N)
humid = np.clip(np.random.uniform(0.2, 0.9, N), 0, 1)
elevs = np.random.uniform(10.0, 80.0, N)

meas = []
corr = []
bias_list = []
for i in range(N):
    inp = DFDInputs(lat=lat, lon=lon, h_m=h_m, temp_K=temps[i],
                    pressure_Pa=press[i], rh_frac=humid[i], elev_deg=elevs[i],
                    range_m=true_range_m)
    out = compute_correction(inp)
    noise = np.random.normal(0.0, 0.5)  # 0.5 m random
    meas_range = true_range_m + out.range_bias_m + noise
    corrected = meas_range - out.range_bias_m

    meas.append(meas_range)
    corr.append(corrected)
    bias_list.append(out.range_bias_m)

df = pd.DataFrame({
    "temp_K": temps,
    "pressure_Pa": press,
    "rh_frac": humid,
    "elev_deg": elevs,
    "true_range_m": true_range_m,
    "measured_range_m": meas,
    "dfd_range_bias_m": bias_list,
    "corrected_range_m": corr
})

df["err_measured_m"] = df["measured_range_m"] - df["true_range_m"]
df["err_corrected_m"] = df["corrected_range_m"] - df["true_range_m"]

rmse_meas = float(np.sqrt(np.mean(df["err_measured_m"]**2)))
rmse_corr = float(np.sqrt(np.mean(df["err_corrected_m"]**2)))
improv = (rmse_meas - rmse_corr) / rmse_meas * 100.0

print(f"RMSE (naive GPS): {rmse_meas:.3f} m")
print(f"RMSE (DFD-corrected): {rmse_corr:.3f} m")
print(f"Relative improvement: {improv:.1f}%")

plt.figure(figsize=(7,4))
bins = np.linspace(-5, 5, 60)
plt.hist(df["err_measured_m"], bins=bins, alpha=0.6, label="Naive GPS error")
plt.hist(df["err_corrected_m"], bins=bins, alpha=0.6, label="DFD-corrected error")
plt.axvline(0, color='k', linestyle='--')
plt.title("Range Error Distribution (Synthetic Demo)")
plt.xlabel("Error (m)")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.savefig("/mnt/data/dfd_gps_webapi/benchmark_error_hist.png", dpi=160)

df.to_csv("/mnt/data/dfd_gps_webapi/benchmark_results.csv", index=False)

# Summary JSON
import json
summary = {
    "RMSE_naive_m": round(rmse_meas, 3),
    "RMSE_DFD_corrected_m": round(rmse_corr, 3),
    "relative_improvement_percent": round(improv, 1)
}
open("/mnt/data/dfd_gps_webapi/benchmark_summary.json", "w").write(json.dumps(summary, indent=2))
