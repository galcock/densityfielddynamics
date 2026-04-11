#!/usr/bin/env python3
"""
Standalone DFD κ_r background-field Monte Carlo for SU(2) gauge sector coupled to integer microlevel k via ψ(k).

True DFD micro-action:
  S = sum_x[-log w(k_x)] + (Kpsi/2) sum_<xy> (ψ_x-ψ_y)^2
      - sum_p β e^{-ψ_p} (1/2) Re Tr[ U_p(theta) ]

Background field in the σ3 (Cartan) direction applied to selected plaquettes:
  U_p(theta) = B(theta) U_p ,  B(theta)=exp(i theta σ3)=cos θ I + i sin θ σ3
Then for U_p written as quaternion: U_p = a0 I + i (a·σ)
  (1/2)Re Tr[B U_p] = a0 cosθ - a3 sinθ.

Thus at θ=0:
  S'  =  sum_p β e^{-ψ_p} a3_p Ω_p
  S'' =  sum_p β e^{-ψ_p} a0_p Ω_p

and F''(0) = <S''> - <(S')^2> + <S'>^2,  κ = F''/V.

This script is a reference implementation to be transplanted into the repo pipeline.

Outputs JSON artifact with κ and blocked SE.

"""
from __future__ import annotations
import json
import os
import argparse, json, numpy as np, math
from dataclasses import dataclass
from dfd_micro_action_kpsi import w_of_k, psi_of_k

PI=np.pi

def idx(x,y,z,L): return x + L*(y + L*z)
def inv_idx(i,L):
    x=i%L; y=(i//L)%L; z=i//(L*L)
    return x,y,z
def mod(a,L): return a%L

# Quaternion utilities for SU(2): q=(a0,a1,a2,a3) with unit norm.
def q_mul(q,p):
    a0,a1,a2,a3=q
    b0,b1,b2,b3=p
    return np.array([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0
    ], dtype=np.float64)

def q_conj(q):
    a0,a1,a2,a3=q
    return np.array([a0,-a1,-a2,-a3], dtype=np.float64)

def q_norm(q): return float(np.sqrt(np.dot(q,q)))

def q_unit(q):
    n=q_norm(q)
    if n==0: 
        return np.array([1.0,0.0,0.0,0.0], dtype=np.float64)
    return q/n

def q_random_near_identity(rng, eps):
    # sample random axis uniformly on S^2 and angle ~ Uniform(-eps,eps)
    v=rng.normal(size=3)
    v=v/np.linalg.norm(v)
    ang=rng.uniform(-eps,eps)
    return np.array([math.cos(ang), *(v*math.sin(ang))], dtype=np.float64)

@dataclass
class Lattice:
    L:int
    V:int
    U:np.ndarray  # shape (V,3,4) quaternions
    k:np.ndarray  # (V,) int
    psi:np.ndarray  # (V,) float

def init_lat(L, seed, k0=8):
    rng=np.random.default_rng(seed)
    V=L**3
    # random SU(2) links via normalized Gaussian quaternion
    U=rng.normal(size=(V,3,4))
    U=U/np.linalg.norm(U, axis=2, keepdims=True)
    U=U.astype(np.float64)
    k=np.full(V,int(k0),dtype=np.int32)
    psi=psi_of_k(k,zeta=1.0,k_ref=1).astype(np.float64)
    return Lattice(L=L,V=V,U=U,k=k,psi=psi)

def neighbor_sites(site,L):
    x,y,z=inv_idx(site,L)
    out=[]
    for dx,dy,dz in [(1,0,0),(0,1,0),(0,0,1)]:
        out.append(idx(mod(x+dx,L),mod(y+dy,L),mod(z+dz,L),L))
        out.append(idx(mod(x-dx,L),mod(y-dy,L),mod(z-dz,L),L))
    return out

def plaquette_sites(site0,mu,nu,L):
    x,y,z=inv_idx(site0,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    dxm,dym,dzm=dirs[mu]; dxn,dyn,dzn=dirs[nu]
    s0=site0
    sm=idx(mod(x+dxm,L),mod(y+dym,L),mod(z+dzm,L),L)
    sn=idx(mod(x+dxn,L),mod(y+dyn,L),mod(z+dzn,L),L)
    smn=idx(mod(x+dxm+dxn,L),mod(y+dym+dyn,L),mod(z+dzm+dzn,L),L)
    return s0,sm,sn,smn

def plaquette_quat(lat: Lattice, site0, mu, nu):
    # U_p = U(s0,mu) U(s0+mu,nu) U(s0+nu,mu)^{-1} U(s0,nu)^{-1}
    L=lat.L
    s0,sm,sn,smn = plaquette_sites(site0,mu,nu,L)
    U1=lat.U[s0,mu]
    U2=lat.U[sm,nu]
    U3=q_conj(lat.U[sn,mu])  # inverse
    U4=q_conj(lat.U[s0,nu])
    Up=q_mul(q_mul(q_mul(U1,U2),U3),U4)
    return q_unit(Up)

def psi_plaquette(lat: Lattice, site0, mu, nu):
    s0,sm,sn,smn = plaquette_sites(site0,mu,nu,lat.L)
    return 0.25*(lat.psi[s0]+lat.psi[sm]+lat.psi[sn]+lat.psi[smn])

def plaquettes_touching_link(site, mu, L):
    # same combinatorics as U(1): for each nu!=mu, plaquette at site and shifted back along nu.
    x,y,z=inv_idx(site,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    out=[]
    for nu in range(3):
        if nu==mu: continue
        out.append((site,mu,nu))
        dx,dy,dz=dirs[nu]
        site0=idx(mod(x-dx,L),mod(y-dy,L),mod(z-dz,L),L)
        out.append((site0,mu,nu))
    return out

def local_gauge_action_for_link(lat: Lattice, site, mu, beta, theta_bg, bg_plane):
    S=0.0
    for (site0,mu0,nu) in plaquettes_touching_link(site,mu,lat.L):
        psi_p=psi_plaquette(lat,site0,mu0,nu)
        Up=plaquette_quat(lat,site0,mu0,nu)
        a0=float(Up[0]); a3=float(Up[3])
        Omega=1.0 if (bg_plane==(mu0,nu) or bg_plane==(nu,mu0)) else 0.0
        # (1/2)ReTr[B U] = a0 cosθ - a3 sinθ, with θ=theta_bg*Omega
        th=theta_bg*Omega
        val=a0*math.cos(th) - a3*math.sin(th)
        S += -beta*math.exp(-psi_p)*val
    return S

def metropolis_link_sweep(lat: Lattice, rng, beta, theta_bg, bg_plane, eps):
    V=lat.V
    acc=0; tot=0
    for s in range(V):
        for mu in range(3):
            tot+=1
            Sold=local_gauge_action_for_link(lat,s,mu,beta,theta_bg,bg_plane)
            Uold=lat.U[s,mu].copy()
            R=q_random_near_identity(rng, eps)
            Unew=q_unit(q_mul(R,Uold))
            lat.U[s,mu]=Unew
            Snew=local_gauge_action_for_link(lat,s,mu,beta,theta_bg,bg_plane)
            dS=Snew-Sold
            if dS<=0 or rng.random()<math.exp(-dS):
                acc+=1
            else:
                lat.U[s,mu]=Uold
    return acc/tot

def plaquettes_touching_site(site,L):
    x,y,z=inv_idx(site,L)
    dirs=[(1,0,0),(0,1,0),(0,0,1)]
    out=set()
    for mu in range(3):
        for nu in range(mu+1,3):
            dxm,dym,dzm=dirs[mu]
            dxn,dyn,dzn=dirs[nu]
            candidates=[
                (x,y,z),
                (mod(x-dxm,L),mod(y-dym,L),mod(z-dzm,L)),
                (mod(x-dxn,L),mod(y-dyn,L),mod(z-dzn,L)),
                (mod(x-dxm-dxn,L),mod(y-dym-dyn,L),mod(z-dzm-dzn,L)),
            ]
            for x0,y0,z0 in candidates:
                out.add((idx(x0,y0,z0,L),mu,nu))
    return list(out)

def local_gauge_action_for_site(lat: Lattice, site, beta, theta_bg, bg_plane):
    S=0.0
    for (site0,mu,nu) in plaquettes_touching_site(site,lat.L):
        psi_p=psi_plaquette(lat,site0,mu,nu)
        Up=plaquette_quat(lat,site0,mu,nu)
        a0=float(Up[0]); a3=float(Up[3])
        Omega=1.0 if (bg_plane==(mu,nu) or bg_plane==(nu,mu)) else 0.0
        th=theta_bg*Omega
        val=a0*math.cos(th) - a3*math.sin(th)
        S += -beta*math.exp(-psi_p)*val
    return S

def local_k_terms(lat: Lattice, site, Kpsi, zeta=1.0, k_ref=1):
    k=int(lat.k[site])
    Sk=-math.log(float(w_of_k(np.asarray([k],dtype=int))[0]))
    psi_s=float(lat.psi[site])
    d2=0.0
    for nb in neighbor_sites(site,lat.L):
        d=psi_s-float(lat.psi[nb])
        d2+=d*d
    Sg=0.5*0.5*float(Kpsi)*d2
    return Sk+Sg

def metropolis_k_sweep(lat: Lattice, rng, Kpsi, beta, theta_bg, bg_plane, zeta=1.0, k_ref=1):
    V=lat.V
    acc=0; tot=0
    for s in range(V):
        tot+=1
        k_old=int(lat.k[s])
        step=1 if rng.random()<0.5 else -1
        k_new=k_old+step
        if k_new<0:
            continue
        aff=[s]+neighbor_sites(s,lat.L)
        Sold_k=sum(local_k_terms(lat,si,Kpsi,zeta=zeta,k_ref=k_ref) for si in aff)
        Sold_g=local_gauge_action_for_site(lat,s,beta,theta_bg,bg_plane)

        lat.k[s]=k_new
        lat.psi[s]=psi_of_k(np.asarray([k_new],dtype=int),zeta=zeta,k_ref=k_ref)[0]

        Snew_k=sum(local_k_terms(lat,si,Kpsi,zeta=zeta,k_ref=k_ref) for si in aff)
        Snew_g=local_gauge_action_for_site(lat,s,beta,theta_bg,bg_plane)

        dS=(Snew_k+Snew_g)-(Sold_k+Sold_g)
        if dS<=0 or rng.random()<math.exp(-dS):
            acc+=1
        else:
            lat.k[s]=k_old
            lat.psi[s]=psi_of_k(np.asarray([k_old],dtype=int),zeta=zeta,k_ref=k_ref)[0]
    return acc/max(tot,1)

def measure_Sprime_Sdprime(lat: Lattice, beta, bg_plane):
    L=lat.L
    Spr=0.0; Sd2=0.0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s0=idx(x,y,z,L)
                for mu in range(3):
                    for nu in range(mu+1,3):
                        Omega=1.0 if (bg_plane==(mu,nu) or bg_plane==(nu,mu)) else 0.0
                        if Omega==0.0: 
                            continue
                        psi_p=psi_plaquette(lat,s0,mu,nu)
                        Up=plaquette_quat(lat,s0,mu,nu)
                        a0=float(Up[0]); a3=float(Up[3])
                        w=beta*math.exp(-psi_p)*Omega
                        # S' = sum β e^{-ψ} a3 Ω ; S'' = sum β e^{-ψ} a0 Ω
                        Spr += w*a3
                        Sd2 += w*a0
    return Spr,Sd2

def blocked_stats(vals, nblock):
    vals=np.asarray(vals,float)
    n=len(vals)
    if nblock<=1 or n<2*nblock:
        m=vals.mean()
        s=vals.std(ddof=1)/np.sqrt(max(n,1))
        return float(m), float(s), int(n)
    b=n//nblock
    blocks=[]
    for i in range(nblock):
        seg=vals[i*b:(i+1)*b]
        if len(seg)==0: continue
        blocks.append(seg.mean())
    blocks=np.asarray(blocks,float)
    m=float(blocks.mean())
    s=float(blocks.std(ddof=1)/np.sqrt(len(blocks)))
    return m,s,int(len(blocks))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--sweeps", type=int, default=2000)
    ap.add_argument("--therm", type=int, default=400)
    ap.add_argument("--measure_every", type=int, default=4)
    ap.add_argument("--seed", type=int, default=20251220)
    ap.add_argument("--k0", type=int, default=8)
    ap.add_argument("--zeta", type=float, default=1.0)
    ap.add_argument("--k_ref", type=int, default=1)
    ap.add_argument("--Kpsi", type=float, default=0.25)
    ap.add_argument("--beta", type=float, default=2.0)
    ap.add_argument("--bg_plane", type=str, default="xy")
    ap.add_argument("--eps", type=float, default=0.35, help="proposal size for SU(2) random rotation")
    ap.add_argument("--out", required=True)
    ap.add_argument("--progress_every", type=int, default=2000)
    ap.add_argument("--checkpoint_every", type=int, default=20000)
    args=ap.parse_args()

    plane_map={"xy":(0,1),"xz":(0,2),"yz":(1,2)}
    if args.bg_plane not in plane_map:
        raise ValueError("bg_plane must be one of xy,xz,yz")
    bg_plane=plane_map[args.bg_plane]

    rng=np.random.default_rng(args.seed)
    lat=init_lat(args.L,args.seed,k0=args.k0)

    Spr_vals=[]; Sd2_vals=[]
    accU=[]; acck=[]
    for sweep in range(args.sweeps):
        if (sweep % args.progress_every) == 0:
            print(f"[{sweep}/{args.sweeps}] running...", flush=True)
        if sweep and (sweep % args.checkpoint_every) == 0:
            outdir = os.path.dirname(args.out)
            if outdir:
                os.makedirs(outdir, exist_ok=True)
            with open(args.out + ".partial", "w") as f:
                json.dump({"sweep": int(sweep), "params": vars(args)}, f, indent=2)
        accU.append(metropolis_link_sweep(lat,rng,args.beta,0.0,bg_plane,args.eps))
        acck.append(metropolis_k_sweep(lat,rng,args.Kpsi,args.beta,0.0,bg_plane,zeta=args.zeta,k_ref=args.k_ref))
        if sweep>=args.therm and ((sweep-args.therm)%args.measure_every==0):
            Spr,Sd2=measure_Sprime_Sdprime(lat,args.beta,bg_plane)
            Spr_vals.append(Spr); Sd2_vals.append(Sd2)

    Spr_vals=np.asarray(Spr_vals,float); Sd2_vals=np.asarray(Sd2_vals,float)
    V=lat.V
    F2 = Sd2_vals.mean() - (Spr_vals**2).mean() + (Spr_vals.mean()**2)
    kappa=float(F2/V)

    f2 = Sd2_vals - Spr_vals**2
    m_f2,se_f2,nb=blocked_stats(f2, nblock=10)
    m_Spr,se_Spr,_=blocked_stats(Spr_vals, nblock=10)
    se_F2=float(np.sqrt(se_f2**2 + (2*m_Spr*se_Spr)**2))
    se_kappa=float(se_F2/V)

    out={
        "tool":"dfd_kappa_backgroundfield_su2_mc",
        "params":vars(args),
        "lattice":{"L":lat.L,"V":lat.V},
        "acceptance":{"U_mean":float(np.mean(accU)),"k_mean":float(np.mean(acck))},
        "measurements":{"n":int(len(Spr_vals)),"measure_every":args.measure_every},
        "estimators":{
            "Spr_mean":float(Spr_vals.mean()),
            "Sd2_mean":float(Sd2_vals.mean()),
            "F2":float(F2),
            "kappa":kappa,
            "kappa_se_block10":se_kappa
        },
        "notes":{
            "background":"Cartan sigma3: (1/2)ReTr[B(theta)U]=a0 cosθ - a3 sinθ for Up=(a0,a)",
            "status":"Reference MC; use long runs and autocorr diagnostics for physics-grade conclusions."
        }
    }
    with open(args.out,"w") as f:
        json.dump(out,f,indent=2)
    print("WROTE", args.out)
    print("kappa", kappa, "+/-", se_kappa)
    print("acc U", float(np.mean(accU)), "acc k", float(np.mean(acck)))

if __name__=="__main__":
    main()
