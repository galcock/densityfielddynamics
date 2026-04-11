#!/usr/bin/env python3
import argparse, math
DM21_BF=7.49e-5; DM21_SIG=0.19e-5
DM3L_BF=2.513e-3; DM3L_SIG=0.5*(0.021e-3+0.019e-3)
DM21_DEF=7.48e-5; DM3L_DEF=2.510e-3

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dm21',type=float,default=DM21_DEF)
    ap.add_argument('--dm3l',type=float,default=DM3L_DEF)
    a=ap.parse_args()
    p21=(a.dm21-DM21_BF)/DM21_SIG
    p3l=(a.dm3l-DM3L_BF)/DM3L_SIG
    chi2=p21*p21+p3l*p3l
    pval=math.exp(-chi2/2.0)
    print('NuFIT 6.0 Table 1 (IC24+SK-atm), Normal Ordering')
    print(f"Δm^2_21: bf={DM21_BF:.5e} σ={DM21_SIG:.2e} pred={a.dm21:.5e} pull={p21:+.3f}σ")
    print(f"Δm^2_3l: bf={DM3L_BF:.5e} σ={DM3L_SIG:.2e} pred={a.dm3l:.5e} pull={p3l:+.3f}σ")
    print(f"χ^2 (2 dof, uncorrelated Gaussian) = {chi2:.4f}")
    print(f"approx p-value (2 dof) = {pval:.4f}")

if __name__=='__main__':
    main()
