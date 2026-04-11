#!/usr/bin/env python3
"""
Run U(1) and SU(2) κ_r background-field MC using true DFD micro-action (k/ψ + derived measure),
then compute α from κ's.

Definitions:
  g1^2 = 1/κ_U1
  g2^2 = 1/κ_SU2
  e^2  = g1^2 g2^2 / (g1^2 + g2^2)
  α    = e^2 / (4π)

Writes:
  artifacts/kappa_u1_*.json
  artifacts/kappa_su2_*.json
  artifacts/alpha_from_kappa_*.json
"""
from __future__ import annotations
import argparse, json, os, subprocess, time, math
import numpy as np

PI=math.pi

def run(cmd):
    p=subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode!=0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}")
    return p.stdout

def delta_method_alpha(k1, s1, k2, s2):
    # g1^2=1/k1; g2^2=1/k2; e2 = (g1^2 g2^2)/(g1^2+g2^2); alpha=e2/(4π)
    g1=1.0/k1
    g2=4.0/k2
    e2=(g1*g2)/(g1+g2)
    alpha=e2/(4*PI)

    # Jacobian wrt k1,k2 via chain rule:
    # g = 1/k -> dg/dk = -1/k^2
    dg1=-1.0/(k1*k1)
    dg2=-4.0/(k2*k2)
    # e2 = (g1 g2)/(g1+g2)
    denom=(g1+g2)
    de_dg1 = (g2*denom - g1*g2*1.0)/ (denom*denom)  # quotient rule
    de_dg2 = (g1*denom - g1*g2*1.0)/ (denom*denom)
    de_dk1 = de_dg1*dg1
    de_dk2 = de_dg2*dg2
    da_dk1 = de_dk1/(4*PI)
    da_dk2 = de_dk2/(4*PI)
    var = (da_dk1*s1)**2 + (da_dk2*s2)**2
    return alpha, math.sqrt(var)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--outdir", default="artifacts")
    ap.add_argument("--tag", default=None, help="optional label for outputs")
    ap.add_argument("--progress_every", type=int, default=2000)
    ap.add_argument("--checkpoint_every", type=int, default=20000)

    # U(1)
    ap.add_argument("--u1_L", type=int, default=8)
    ap.add_argument("--u1_sweeps", type=int, default=60000)
    ap.add_argument("--u1_therm", type=int, default=10000)
    ap.add_argument("--u1_meas", type=int, default=10)
    ap.add_argument("--u1_beta", type=float, default=1.0)
    ap.add_argument("--u1_Kpsi", type=float, default=0.25)
    ap.add_argument("--u1_k0", type=int, default=8)
    ap.add_argument("--u1_seed", type=int, default=1)
    # SU(2)
    ap.add_argument("--su2_L", type=int, default=8)
    ap.add_argument("--su2_sweeps", type=int, default=60000)
    ap.add_argument("--su2_therm", type=int, default=10000)
    ap.add_argument("--su2_meas", type=int, default=10)
    ap.add_argument("--su2_beta", type=float, default=2.0)
    ap.add_argument("--su2_eps", type=float, default=0.35)
    ap.add_argument("--su2_Kpsi", type=float, default=0.25)
    ap.add_argument("--su2_k0", type=int, default=8)
    ap.add_argument("--su2_seed", type=int, default=2)
    args=ap.parse_args()

    outdir=args.outdir
    os.makedirs(outdir, exist_ok=True)
    tag = args.tag or time.strftime("%Y%m%d_%H%M%S")

    u1_out=os.path.join(outdir, f"kappa_u1_{tag}.json")
    su2_out=os.path.join(outdir, f"kappa_su2_{tag}.json")
    alpha_out=os.path.join(outdir, f"alpha_from_kappa_{tag}.json")

    # Run U(1)
    run(["python3","dfd_kappa_backgroundfield_u1_mc.py",
         "--L",str(args.u1_L),
         "--sweeps",str(args.u1_sweeps),
         "--therm",str(args.u1_therm),
         "--measure_every",str(args.u1_meas),
         "--seed",str(args.u1_seed),
         "--k0",str(args.u1_k0),
         "--Kpsi",str(args.u1_Kpsi),
         "--beta",str(args.u1_beta),
         "--bg_plane","xy",
         "--out",u1_out,
         "--progress_every",str(args.progress_every),
         "--checkpoint_every",str(args.checkpoint_every)])

    # Run SU(2)
    run(["python3","dfd_kappa_backgroundfield_su2_mc.py",
         "--L",str(args.su2_L),
         "--sweeps",str(args.su2_sweeps),
         "--therm",str(args.su2_therm),
         "--measure_every",str(args.su2_meas),
         "--seed",str(args.su2_seed),
         "--k0",str(args.su2_k0),
         "--Kpsi",str(args.su2_Kpsi),
         "--beta",str(args.su2_beta),
         "--eps",str(args.su2_eps),
         "--bg_plane","xy",
         "--out",su2_out,
         "--progress_every",str(args.progress_every),
         "--checkpoint_every",str(args.checkpoint_every)])

    u1=json.load(open(u1_out))
    su2=json.load(open(su2_out))
    k1=u1["estimators"]["kappa"]; s1=u1["estimators"]["kappa_se_block10"]
    k2=su2["estimators"]["kappa"]; s2=su2["estimators"]["kappa_se_block10"]

    # Compute α
    g1=1.0/k1
    g2=4.0/k2
    e2=(g1*g2)/(g1+g2)
    alpha=e2/(4*PI)
    alpha_se = delta_method_alpha(k1,s1,k2,s2)[1]

    out={
        "tool":"alpha_from_kappa_runner",
        "tag":tag,
        "inputs":{"u1_json":u1_out,"su2_json":su2_out},
        "definitions":{
            "g1_sq":"1/kappa_u1",
            "g2_sq":"1/kappa_su2",
            "e_sq":"g1_sq*g2_sq/(g1_sq+g2_sq)",
            "alpha":"e_sq/(4*pi)"
        },
        "results":{
            "kappa_u1":k1, "kappa_u1_se":s1,
            "kappa_su2":k2, "kappa_su2_se":s2,
            "alpha":alpha, "alpha_se_delta":alpha_se
        },
        "status":"PENDING_PHYSICS until production stats + autocorr checks; file is machine-verifiable."
    }
    with open(alpha_out,"w") as f:
        json.dump(out,f,indent=2)
    print("WROTE", alpha_out)
    print("alpha", alpha, "+/-", alpha_se)

if __name__=="__main__":
    main()
