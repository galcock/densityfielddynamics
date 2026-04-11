#!/usr/bin/env python3
"""
Standalone DFD κ_r background-field Monte Carlo for U(1) gauge sector coupled to integer microlevel k via ψ(k).

Implements the true DFD micro-action:
  S = sum_x[-log w(k_x)] + (Kpsi/2) sum_<xy> (ψ_x-ψ_y)^2 - sum_p β e^{-ψ_p} cos(θ_p + θ_bg Ω_p)

κ is extracted at θ_bg=0 via:
  F(θ) = -log Z(θ)
  F''(0) = <S''> - <(S')^2> + <S'>^2
  κ = F''(0) / V

where for this action at θ_bg=0:
  S'  =  sum_p β e^{-ψ_p} sin(θ_p) Ω_p
  S'' =  sum_p β e^{-ψ_p} cos(θ_p) Ω_p^2

We choose Ω_p=1 for all plaquettes of a chosen orientation (default: xy), else 0.

Outputs a JSON artifact with κ estimate and blocked standard error.

NOTE: This is a reference implementation intended to be transplanted into the repo pipeline.
"""

from __future__ import annotations
import json
import os
import argparse, json, numpy as np
from dataclasses import dataclass

from dfd_micro_action_kpsi import w_of_k, psi_of_k

PI = np.pi

def idx(x,y,z,L):
    return x + L*(y + L*z)

def inv_idx(i,L):
    x = i % L
    y = (i//L) % L
    z = i//(L*L)
    return x,y,z

def mod(a,L): 
    return a % L

@dataclass
class Lattice:
    L: int
    V: int
    # gauge links: angles A[site, mu] with mu=0,1,2
    A: np.ndarray
    # integer k per site
    k: np.ndarray
    # cached psi per site
    psi: np.ndarray

def init_lattice(L, seed, k0=8):
    rng = np.random.default_rng(seed)
    V=L**3
    A = rng.uniform(-PI, PI, size=(V,3)).astype(np.float64)
    k = np.full(V, int(k0), dtype=np.int32)
    psi = psi_of_k(k, zeta=1.0, k_ref=1).astype(np.float64)
    return Lattice(L=L, V=V, A=A, k=k, psi=psi)

def neighbor_sites(site, L):
    x,y,z=inv_idx(site,L)
    out=[]
    for mu,(dx,dy,dz) in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
        xp,yp,zp=mod(x+dx,L),mod(y+dy,L),mod(z+dz,L)
        xm,ym,zm=mod(x-dx,L),mod(y-dy,L),mod(z-dz,L)
        out.append(idx(xp,yp,zp,L))
        out.append(idx(xm,ym,zm,L))
    return out  # length 6

def plaquettes_touching_link(site, mu, L):
    """
    Return list of plaquettes that include link (site,mu). Each plaquette is represented by
    (site0, mu, nu, orientation_sign) where plaquette angle is:
      θ_p = A(site0,mu) + A(site0+mu,nu) - A(site0+nu,mu) - A(site0,nu)
    orientation_sign is +1 for the canonical order above.
    """
    x,y,z=inv_idx(site,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    out=[]
    for nu in range(3):
        if nu==mu: 
            continue
        # plaquette with corners at site in (mu,nu) plane
        out.append((site, mu, nu, +1))
        # plaquette shifted back along nu includes the same link
        dx,dy,dz=dirs[nu]
        x0,y0,z0=mod(x-dx,L),mod(y-dy,L),mod(z-dz,L)
        site0=idx(x0,y0,z0,L)
        out.append((site0, mu, nu, +1))
    return out  # 4 plaquettes in 3D

def plaquette_sites(site0, mu, nu, L):
    x,y,z=inv_idx(site0,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    dxm,dym,dzm=dirs[mu]
    dxn,dyn,dzn=dirs[nu]
    s0=site0
    sm=idx(mod(x+dxm,L), mod(y+dym,L), mod(z+dzm,L), L)
    sn=idx(mod(x+dxn,L), mod(y+dyn,L), mod(z+dzn,L), L)
    smn=idx(mod(x+dxm+dxn,L), mod(y+dym+dyn,L), mod(z+dzm+dzn,L), L)
    return (s0, sm, sn, smn)

def plaquette_angle(lat: Lattice, site0, mu, nu):
    L=lat.L
    x,y,z=inv_idx(site0,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    dxm,dym,dzm=dirs[mu]
    dxn,dyn,dzn=dirs[nu]
    s0=site0
    sm=idx((x+dxm)%L,(y+dym)%L,(z+dzm)%L,L)
    sn=idx((x+dxn)%L,(y+dyn)%L,(z+dzn)%L,L)
    # θ = A(s0,mu) + A(s0+mu,nu) - A(s0+nu,mu) - A(s0,nu)
    th = lat.A[s0,mu] + lat.A[sm,nu] - lat.A[sn,mu] - lat.A[s0,nu]
    # wrap to (-pi,pi] for numerical stability
    th = (th + PI)%(2*PI) - PI
    return th

def psi_plaquette(lat: Lattice, site0, mu, nu):
    s0, sm, sn, smn = plaquette_sites(site0, mu, nu, lat.L)
    return 0.25*(lat.psi[s0]+lat.psi[sm]+lat.psi[sn]+lat.psi[smn])

def local_gauge_action_for_link(lat: Lattice, site, mu, beta, theta_bg, bg_plane):
    """
    Sum gauge action contributions of plaquettes touching link (site,mu).
    """
    S=0.0
    for (site0, mu0, nu, sgn) in plaquettes_touching_link(site, mu, lat.L):
        th = plaquette_angle(lat, site0, mu0, nu)
        psi_p = psi_plaquette(lat, site0, mu0, nu)
        Omega = 1.0 if (bg_plane==(mu0,nu) or bg_plane==(nu,mu0)) else 0.0
        S += -beta*np.exp(-psi_p)*np.cos(th + theta_bg*Omega)
    return S

def metropolis_link_update(lat: Lattice, rng, beta, theta_bg, bg_plane, step=0.3):
    """
    Single sweep over all links.
    """
    V=lat.V
    acc=0; tot=0
    for s in range(V):
        for mu in range(3):
            tot += 1
            old = lat.A[s,mu]
            Sold = local_gauge_action_for_link(lat, s, mu, beta, theta_bg, bg_plane)
            prop = old + rng.uniform(-step, step)
            prop = (prop + PI)%(2*PI) - PI
            lat.A[s,mu]=prop
            Snew = local_gauge_action_for_link(lat, s, mu, beta, theta_bg, bg_plane)
            dS = Snew - Sold
            if dS <= 0 or rng.random() < np.exp(-dS):
                acc += 1
            else:
                lat.A[s,mu]=old
    return acc/tot

def local_k_terms(lat: Lattice, site, Kpsi, zeta=1.0, k_ref=1):
    """
    Compute local contribution of k/psi action involving this site:
      -log w(k_site) plus (Kpsi/2)*sum_{neighbors} (psi_site-psi_nb)^2 with 1/2 to avoid double count in Δ.
    We'll return the full sum over the 6 neighbors but include 1/2 factor so the site-local sum is consistent.
    """
    k = int(lat.k[site])
    Sk = -math.log(float(w_of_k(np.asarray([k],dtype=int))[0]))
    psi_s = float(lat.psi[site])
    nbs = neighbor_sites(site, lat.L)
    d2=0.0
    for nb in nbs:
        d = psi_s - float(lat.psi[nb])
        d2 += d*d
    Sg = 0.5*0.5*float(Kpsi)*d2  # 0.5 for the action prefactor, 0.5 for half-counting edges at the site
    return Sk + Sg

def plaquettes_touching_site(site, L):
    """
    Return a list of plaquettes (site0, mu, nu) whose corner set includes site.
    Brute force: enumerate plaquettes with site as one of 4 corners by shifting site0.
    """
    x,y,z=inv_idx(site,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    out=set()
    for mu in range(3):
        for nu in range(mu+1,3):
            # site could be s0, s0+mu, s0+nu, s0+mu+nu
            dxm,dym,dzm=dirs[mu]
            dxn,dyn,dzn=dirs[nu]
            candidates=[
                (x,y,z),
                (mod(x-dxm,L), mod(y-dym,L), mod(z-dzm,L)),
                (mod(x-dxn,L), mod(y-dyn,L), mod(z-dzn,L)),
                (mod(x-dxm-dxn,L), mod(y-dym-dyn,L), mod(z-dzm-dzn,L)),
            ]
            for (x0,y0,z0) in candidates:
                out.add((idx(x0,y0,z0,L), mu, nu))
    return list(out)

def local_gauge_action_for_site(lat: Lattice, site, beta, theta_bg, bg_plane):
    """
    Sum gauge action of all plaquettes that include this site (to update k -> psi and hence psi_p).
    """
    S=0.0
    for (site0, mu, nu) in plaquettes_touching_site(site, lat.L):
        th = plaquette_angle(lat, site0, mu, nu)
        psi_p = psi_plaquette(lat, site0, mu, nu)
        Omega = 1.0 if (bg_plane==(mu,nu) or bg_plane==(nu,mu)) else 0.0
        S += -beta*np.exp(-psi_p)*np.cos(th + theta_bg*Omega)
    return S

def metropolis_k_update(lat: Lattice, rng, Kpsi, beta, theta_bg, bg_plane, zeta=1.0, k_ref=1):
    """
    Single sweep over sites proposing k -> k±1.
    """
    V=lat.V
    acc=0; tot=0
    for s in range(V):
        tot += 1
        k_old = int(lat.k[s])
        # propose +/- 1
        step = 1 if rng.random()<0.5 else -1
        k_new = k_old + step
        if k_new < 0:
            continue
        # local action parts affected by k_s: its own k terms, neighbor gradient contributions, and adjacent plaquettes.
        # We compute a conservative local Δ by recomputing:
        # - k terms at s and its neighbors (because their half-counted edge term changes)
        # - gauge action of plaquettes touching s
        # This is correct because only edges and plaquettes involving s change.
        sites_affected = [s] + neighbor_sites(s, lat.L)
        Sold_k = sum(local_k_terms(lat, si, Kpsi, zeta=zeta, k_ref=k_ref) for si in sites_affected)
        Sold_g = local_gauge_action_for_site(lat, s, beta, theta_bg, bg_plane)

        # apply proposal
        lat.k[s]=k_new
        lat.psi[s]=psi_of_k(np.asarray([k_new],dtype=int), zeta=zeta, k_ref=k_ref)[0]

        Snew_k = sum(local_k_terms(lat, si, Kpsi, zeta=zeta, k_ref=k_ref) for si in sites_affected)
        Snew_g = local_gauge_action_for_site(lat, s, beta, theta_bg, bg_plane)

        dS = (Snew_k + Snew_g) - (Sold_k + Sold_g)
        if dS <= 0 or rng.random() < np.exp(-dS):
            acc += 1
        else:
            # revert
            lat.k[s]=k_old
            lat.psi[s]=psi_of_k(np.asarray([k_old],dtype=int), zeta=zeta, k_ref=k_ref)[0]
    return acc/max(tot,1)

def measure_Sprime_Sdprime(lat: Lattice, beta, bg_plane):
    """
    Measure S' and S'' at theta_bg=0 for κ extraction.
    We sum over all plaquettes with Ω_p=1 for the chosen background plane; Ω=0 otherwise.
    """
    L=lat.L
    Spr=0.0
    Sd2=0.0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s0=idx(x,y,z,L)
                for mu in range(3):
                    for nu in range(mu+1,3):
                        Omega = 1.0 if (bg_plane==(mu,nu) or bg_plane==(nu,mu)) else 0.0
                        if Omega==0.0:
                            continue
                        th=plaquette_angle(lat,s0,mu,nu)
                        psi_p=psi_plaquette(lat,s0,mu,nu)
                        w = beta*np.exp(-psi_p)*Omega
                        Spr += w*np.sin(th)
                        Sd2 += w*np.cos(th)*Omega
    return Spr, Sd2

def blocked_stats(vals, nblock):
    vals=np.asarray(vals,float)
    n=len(vals)
    if nblock<=1 or n<2*nblock:
        m=vals.mean()
        s=vals.std(ddof=1)/np.sqrt(max(n,1))
        return float(m), float(s), int(n)
    b = n//nblock
    blocks=[]
    for i in range(nblock):
        seg = vals[i*b:(i+1)*b]
        if len(seg)==0: 
            continue
        blocks.append(seg.mean())
    blocks=np.asarray(blocks,float)
    m=float(blocks.mean())
    s=float(blocks.std(ddof=1)/np.sqrt(len(blocks)))
    return m,s,int(len(blocks))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=6)
    ap.add_argument("--sweeps", type=int, default=5000)
    ap.add_argument("--therm", type=int, default=1000)
    ap.add_argument("--measure_every", type=int, default=5)
    ap.add_argument("--seed", type=int, default=20251220)
    ap.add_argument("--k0", type=int, default=8)
    ap.add_argument("--zeta", type=float, default=1.0)
    ap.add_argument("--k_ref", type=int, default=1)
    ap.add_argument("--Kpsi", type=float, default=0.25)
    ap.add_argument("--beta", type=float, default=1.0)
    ap.add_argument("--bg_plane", type=str, default="xy", help="xy, xz, yz")
    ap.add_argument("--link_step", type=float, default=0.35)
    ap.add_argument("--out", required=True)
    ap.add_argument("--progress_every", type=int, default=2000)
    ap.add_argument("--checkpoint_every", type=int, default=20000)
    args=ap.parse_args()

    plane_map={"xy":(0,1),"xz":(0,2),"yz":(1,2)}
    if args.bg_plane not in plane_map:
        raise ValueError("bg_plane must be one of xy,xz,yz")
    bg_plane=plane_map[args.bg_plane]

    rng=np.random.default_rng(args.seed)
    lat=init_lattice(args.L, args.seed, k0=args.k0)

    Spr_vals=[]
    Sd2_vals=[]
    acc_link=[]
    acc_k=[]
    for sweep in range(args.sweeps):
        if (sweep % args.progress_every) == 0:
            print(f"[{sweep}/{args.sweeps}] running...", flush=True)
        if sweep and (sweep % args.checkpoint_every) == 0:
            outdir = os.path.dirname(args.out)
            if outdir:
                os.makedirs(outdir, exist_ok=True)
            with open(args.out + ".partial", "w") as f:
                json.dump({"sweep": int(sweep), "params": vars(args)}, f, indent=2)
        acc_link.append(metropolis_link_update(lat, rng, args.beta, 0.0, bg_plane, step=args.link_step))
        acc_k.append(metropolis_k_update(lat, rng, args.Kpsi, args.beta, 0.0, bg_plane, zeta=args.zeta, k_ref=args.k_ref))
        if sweep >= args.therm and ((sweep-args.therm) % args.measure_every==0):
            Spr,Sd2=measure_Sprime_Sdprime(lat, args.beta, bg_plane)
            Spr_vals.append(Spr)
            Sd2_vals.append(Sd2)

    Spr_vals=np.asarray(Spr_vals,float)
    Sd2_vals=np.asarray(Sd2_vals,float)
    V=lat.V

    # F'' = <S''> - <(S')^2> + <S'>^2
    F2 = Sd2_vals.mean() - (Spr_vals**2).mean() + (Spr_vals.mean()**2)
    kappa = float(F2 / V)

    # Error bar by blocking the per-measurement estimator of F2:
    # define f2_i = Sd2_i - Spr_i^2, then F2 = <f2> + <Spr>^2
    f2 = Sd2_vals - Spr_vals**2
    m_f2, se_f2, nb = blocked_stats(f2, nblock=10)
    m_Spr, se_Spr, _ = blocked_stats(Spr_vals, nblock=10)
    # propagate: F2 = m_f2 + m_Spr^2 with delta method
    se_F2 = float(np.sqrt(se_f2**2 + (2*m_Spr*se_Spr)**2))
    se_kappa = float(se_F2 / V)

    out={
        "tool":"dfd_kappa_backgroundfield_u1_mc",
        "params": vars(args),
        "lattice":{"L":lat.L,"V":lat.V},
        "acceptance":{"link_mean":float(np.mean(acc_link)),"k_mean":float(np.mean(acc_k))},
        "measurements":{"n":int(len(Spr_vals)),"measure_every":args.measure_every},
        "estimators":{
            "Spr_mean":float(Spr_vals.mean()),
            "Sd2_mean":float(Sd2_vals.mean()),
            "F2":float(F2),
            "kappa":kappa,
            "kappa_se_block10":se_kappa
        },
        "notes":{
            "kappa_definition":"kappa = F''(0)/V where F=-log Z(theta) and theta couples to selected plaquettes via cos(theta_p+theta*Omega_p)",
            "status":"This output is a Monte Carlo estimate for U(1) only. Use long runs and autocorr diagnostics for physics-grade conclusions."
        }
    }
    with open(args.out,"w") as f:
        json.dump(out,f,indent=2)
    print("WROTE", args.out)
    print("kappa", kappa, "+/-", se_kappa)
    print("acc link", float(np.mean(acc_link)), "acc k", float(np.mean(acc_k)))

if __name__=="__main__":
    import math
    main()
