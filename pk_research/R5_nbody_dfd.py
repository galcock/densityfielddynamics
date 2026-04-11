#!/usr/bin/env python3
"""
R5_nbody_dfd.py — DFD Particle-Mesh N-body Simulation
======================================================
Full nonlinear MOND field equation with self-consistent sigma_nabla regulation.

Physics:
  div[mu(|grad Phi_eff|/(2a0)) grad Phi] = (3/2)*Omega_b*H0^2/a * delta

The KEY DFD insight (sigma_nabla regulation):
  The MOND interpolation function mu sees the TOTAL field gradient, including
  the cosmological background from the Hubble flow:
    |grad Phi_eff| = sqrt(|grad Phi_pert|^2 + a_ext^2)
  where a_ext = c*H(z) is the "external field" from the expanding universe.
  This keeps x_bar = c*H/(2*a0) ~ 3 (at z=0), so mu ~ 0.75.

  Without this regulation, perturbation gradients alone give x ~ 10^{-4},
  meaning mu ~ 10^{-4} and gravity is boosted by ~10^4 — catastrophic.

Three runs: DFD (with EFE), Newtonian (mu=1), LCDM.
64^3, z=49 -> z=0, 200 steps.
"""

import numpy as np
from scipy.fft import fftn, ifftn, fftfreq
from scipy.integrate import solve_ivp
import time, json, os

# ============================================================
# Constants
# ============================================================
Mpc_m   = 3.0857e22
c_SI    = 2.998e8          # m/s
a0_SI   = 1.2e-10          # m/s^2
h_hub   = 0.674

# Code units: positions Mpc/h, velocities km/s, potential (km/s)^2
# acceleration: (km/s)^2 / (Mpc/h)
_acc    = (1e3)**2 / (Mpc_m/h_hub)   # ~ 2.184e-17 m/s^2 per code unit
a0_code = a0_SI / _acc                # ~ 5.49e6

# c in code units: km/s
c_code = c_SI / 1e3  # = 2.998e5 km/s

Omega_b  = 0.049;  Omega_Lb = 1-Omega_b
Omega_mL = 0.315;  Omega_LL = 0.685

NG=64; NP1=64; NP=NP1**3; L=500.0; DX=L/NG
ZI=49.0; NS=200
ZOUT=[10.0, 5.0, 2.0, 1.0, 0.5, 0.0]
H0SQ=1e4  # (100 km/s / (Mpc/h))^2

print(f"a0_code = {a0_code:.3e}")
print(f"c_code  = {c_code:.3e} km/s")
print(f"Grid {NG}^3, L={L}, DX={DX:.2f} Mpc/h, NP={NP}")

# The cosmological EFE:
# a_ext(z) = c * H(z) in physical units
# In code units: H(z) = 100*E(z) km/s/(Mpc/h), so a_ext = c_code * 100*E(z) km/s / (Mpc/h)
# => a_ext in code accel units = c_code * 100 * E(z)  [(km/s)^2 / (Mpc/h)]
# x_bar = a_ext / (2*a0_code) = c_code * 100 * E(z) / (2*a0_code)

def x_bar_of_z(z, Om, OL):
    """x_bar = c*H(z) / (2*a0) — the cosmological EFE."""
    E = np.sqrt(Om*(1+z)**3 + OL)
    H_code = 100 * E  # km/s per Mpc/h
    a_ext = c_code * H_code  # (km/s)^2 / (Mpc/h)
    return a_ext / (2*a0_code)

x0 = x_bar_of_z(0, Omega_b, Omega_Lb)
mu0 = x0/(1+x0)
print(f"x_bar(z=0) = {x0:.4f}, mu(x_bar) = {mu0:.4f}")
print(f"G_eff/G = 1/mu = {1/mu0:.4f}")
x49 = x_bar_of_z(49, Omega_b, Omega_Lb)
print(f"x_bar(z=49) = {x49:.4f}, mu(x_bar) = {x49/(1+x49):.4f}")

# ============================================================
# Growth factor, transfer functions, etc.
# ============================================================
def growth_D(Om,OL):
    def rhs(t,y):
        a=np.exp(t);E2=Om/a**3+OL;q=-1.5*Om/(a**3*E2)
        return [y[1],-(2+q)*y[1]+1.5*Om/(a**3*E2)*y[0]]
    s=solve_ivp(rhs,[np.log(1e-5),0],[1e-5,1e-5],rtol=1e-11,atol=1e-14,
                method='DOP853',dense_output=True)
    D0=s.sol(0)[0]
    def D(a): return s.sol(np.log(np.clip(a,1e-5,1)))[0]/D0
    return D

def T_BBKS(k,Om,h):
    G=Om*h;q=k/(G+1e-30)
    return np.log(1+2.34*q)/(2.34*q+1e-30)*(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**(-0.25)

def T_EH(k,Om,h):
    Omh2=Om*h**2;th=2.7255/2.7
    s=44.5*np.log(9.83/(Omh2+1e-30))/np.sqrt(1+10*(0.6*Omh2)**0.75)
    ag=1-0.328*np.log(431*Omh2)*Omh2/(Omh2+1e-30)+0.38*np.log(22.3*Omh2)
    Ge=Om*h*(ag+(1-ag)/(1+(0.43*k*s)**4))
    q=k*th**2/(Ge+1e-30);Lv=np.log(2*np.e+1.8*q);C=14.2+731/(1+62.5*q)
    return Lv/(Lv+C*q**2)

def sig_R(k,P,R):
    kR=k*R;W=np.where(kR>1e-6,3*(np.sin(kR)-kR*np.cos(kR))/kR**3,1.0)
    dlnk=np.diff(np.log(k),prepend=np.log(k[0])-0.1)
    return np.sqrt(np.sum(P*W**2*k**3*dlnk/(2*np.pi**2)))

def Pk_z0_1d(Om,h,s8):
    ns=0.965;k=np.logspace(-4,1,5000)
    Tk=T_BBKS(k,Om,h) if Om<0.1 else T_EH(k,Om,h)
    P=k**ns*Tk**2;s=sig_R(k,P,8.0);P*=(s8/s)**2 if s>0 else 1.0
    return k,P

# ============================================================
# Initial conditions
# ============================================================
def gen_ICs(Om,OL,s8,seed=42):
    np.random.seed(seed)
    Df=growth_D(Om,OL);ai=1/(1+ZI);Di=Df(ai)
    E2i=Om/ai**3+OL;fi=(Om/(ai**3*E2i))**0.55;Hi=100*np.sqrt(E2i)
    print(f"  D={Di:.6f} f={fi:.4f} H={Hi:.1f}")

    kx=2*np.pi*fftfreq(NG,d=DX)
    KX,KY,KZ=np.meshgrid(kx,kx,kx,indexing='ij')
    K2=KX**2+KY**2+KZ**2;K=np.sqrt(K2);K[0,0,0]=1
    k1d,P1d=Pk_z0_1d(Om,h_hub,s8)
    Pk3=np.interp(K.ravel(),k1d,P1d,left=0,right=0).reshape(K.shape)
    Pk3[0,0,0]=0;Pki=Pk3*Di**2
    V=L**3;amp=np.sqrt(Pki*NG**6/(2*V))
    g1=np.random.standard_normal((NG,NG,NG))
    g2=np.random.standard_normal((NG,NG,NG))
    dk=amp*(g1+1j*g2);dk[0,0,0]=0

    K2s=K2.copy();K2s[0,0,0]=1
    Sx=np.real(ifftn(-1j*KX/K2s*dk))
    Sy=np.real(ifftn(-1j*KY/K2s*dk))
    Sz=np.real(ifftn(-1j*KZ/K2s*dk))
    print(f"  delta_rms={np.std(np.real(ifftn(dk))):.6f} max|Psi|={max(np.max(np.abs(a)) for a in [Sx,Sy,Sz]):.4f}")

    c=DX;x1=np.arange(NG)*c+.5*c
    gx,gy,gz=np.meshgrid(x1,x1,x1,indexing='ij')
    pos=np.column_stack([(gx.ravel()+Sx.ravel())%L,(gy.ravel()+Sy.ravel())%L,(gz.ravel()+Sz.ravel())%L])
    vf=ai*Hi*fi
    vel=np.column_stack([vf*Sx.ravel(),vf*Sy.ravel(),vf*Sz.ravel()])
    print(f"  vel_rms={np.sqrt(np.mean(vel**2)):.2f} km/s")
    return pos,vel

# ============================================================
# CIC deposit / interpolate
# ============================================================
def cic_dep(pos,N,L):
    rho=np.zeros((N,N,N));inv=N/L
    px,py,pz=pos[:,0]*inv,pos[:,1]*inv,pos[:,2]*inv
    ix,iy,iz=np.floor(px).astype(int)%N,np.floor(py).astype(int)%N,np.floor(pz).astype(int)%N
    fx,fy,fz=px-np.floor(px),py-np.floor(py),pz-np.floor(pz)
    for di in range(2):
        wx=(1-fx) if di==0 else fx
        for dj in range(2):
            wy=(1-fy) if dj==0 else fy
            for dk in range(2):
                wz=(1-fz) if dk==0 else fz
                np.add.at(rho,((ix+di)%N,(iy+dj)%N,(iz+dk)%N),wx*wy*wz)
    return rho*(N**3/len(pos))

def cic_int(Fx,Fy,Fz,pos,N,L):
    inv=N/L;px,py,pz=pos[:,0]*inv,pos[:,1]*inv,pos[:,2]*inv
    ix,iy,iz=np.floor(px).astype(int)%N,np.floor(py).astype(int)%N,np.floor(pz).astype(int)%N
    fx,fy,fz=px-np.floor(px),py-np.floor(py),pz-np.floor(pz)
    ax=np.zeros(len(pos));ay=ax.copy();az=ax.copy()
    for di in range(2):
        wx=(1-fx) if di==0 else fx
        for dj in range(2):
            wy=(1-fy) if dj==0 else fy
            for dk in range(2):
                wz=(1-fz) if dk==0 else fz
                w=wx*wy*wz;ii=(ix+di)%N;jj=(iy+dj)%N;kk=(iz+dk)%N
                ax+=w*Fx[ii,jj,kk];ay+=w*Fy[ii,jj,kk];az+=w*Fz[ii,jj,kk]
    return ax,ay,az

# ============================================================
# Poisson solvers
# ============================================================
_K2={}
def poisson(delta,pf,N,L):
    key=(N,L)
    if key not in _K2:
        kx=2*np.pi*fftfreq(N,d=L/N);A,B,C=np.meshgrid(kx,kx,kx,indexing='ij')
        K2=A**2+B**2+C**2;K2[0,0,0]=1;_K2[key]=K2
    dk=fftn(delta);r=-pf*dk/_K2[key];r[0,0,0]=0
    return np.real(ifftn(r))

def grad3(f,h):
    return ((np.roll(f,-1,0)-np.roll(f,1,0))/(2*h),
            (np.roll(f,-1,1)-np.roll(f,1,1))/(2*h),
            (np.roll(f,-1,2)-np.roll(f,1,2))/(2*h))
def div3(fx,fy,fz,h):
    return ((np.roll(fx,-1,0)-np.roll(fx,1,0))+
            (np.roll(fy,-1,1)-np.roll(fy,1,1))+
            (np.roll(fz,-1,2)-np.roll(fz,1,2)))/(2*h)

def solve_MOND_EFE(delta, pf, N, L, z, Om, OL, tol=5e-3, maxit=200, w0=0.06):
    """
    Solve the DFD modified Poisson equation WITH cosmological EFE:

    div[mu(x_eff) * grad Phi] = pf * delta

    where x_eff = sqrt(|grad Phi|^2 + a_ext^2) / (2*a0)
    and a_ext = c*H(z) is the Hubble flow external field.

    The EFE ensures mu is always > mu(x_bar) ~ 0.75, preventing the
    deep-MOND catastrophe on cosmological scales.
    """
    h = L/N
    S = pf * delta
    Srms = np.sqrt(np.mean(S**2)) + 1e-30

    # External field in code acceleration units
    E_z = np.sqrt(Om*(1+z)**3 + OL)
    H_z = 100 * E_z  # km/s per Mpc/h
    a_ext = c_code * H_z  # (km/s)^2 / (Mpc/h) — Hubble flow "external" acceleration
    a_ext_sq = a_ext**2

    # x_bar = a_ext / (2*a0)
    xb = a_ext / (2*a0_code)
    mu_bg = xb/(1+xb)

    # Starting guess: Newtonian / mu_bg (since mu is roughly uniform at mu_bg)
    Phi = poisson(delta, pf, N, L) / mu_bg

    best_rel = 1e30; bestPhi = Phi.copy()
    om = w0

    for it in range(maxit):
        gx,gy,gz = grad3(Phi,h)
        grad_sq = gx**2+gy**2+gz**2
        # Effective gradient includes external field (added in quadrature)
        geff = np.sqrt(grad_sq + a_ext_sq)
        x = geff / (2*a0_code)
        mu = x / (1+x)

        lhs = div3(mu*gx, mu*gy, mu*gz, h)
        res = lhs - S
        rel = np.sqrt(np.mean(res**2)) / Srms

        if rel < best_rel:
            best_rel = rel; bestPhi = Phi.copy()
        if rel < tol:
            break
        if it > 30 and rel > 5*best_rel:
            om *= 0.5; Phi = bestPhi.copy()
            if om < 1e-5: break
            continue

        # Diagonal of linearised operator
        # d(mu)/d(|grad Phi|^2) = (1/(2*a0)) * 1/(1+x)^2 * grad_sq/geff
        # But for diagonal, use mu_eff ~ mu + correction
        mup = 1/(1+x)**2
        # Chain rule: dmu/d(grad_Phi_i) = mup * geff/(2*a0) * (grad_Phi_i / geff)
        # Diagonal contribution: mu + mup * grad_sq / (geff * 2*a0)
        mue = np.maximum(mu + mup * grad_sq / (geff * 2*a0_code + 1e-30), 1e-4)
        diag = mue * 6.0/h**2
        Phi -= om * res / diag

    Phi = bestPhi

    # Final diagnostics
    gx,gy,gz = grad3(Phi,h)
    grad_sq = gx**2+gy**2+gz**2
    gm_pert = np.sqrt(grad_sq)
    geff = np.sqrt(grad_sq + a_ext_sq)
    x = geff/(2*a0_code)
    mu_f = x/(1+x)

    # The "MOND enhancement" is the ratio of DFD force to Newtonian force
    # For a mode delta, Newtonian gives Phi_N = -pf*delta/k^2
    # DFD gives Phi_DFD ~ Phi_N / mu_eff
    # So the enhancement factor is 1/mu_eff on average

    info = {'it':it+1, 'rel':float(best_rel),
            'x_bar':float(xb), 'mu_bg':float(mu_bg),
            'x_eff_bar':float(np.mean(x)),
            'mu_eff_bar':float(np.mean(mu_f)), 'mu_eff_med':float(np.median(mu_f)),
            'grad_pert_rms':float(np.sqrt(np.mean(grad_sq))),
            'a_ext':float(a_ext),
            'Geff_over_G': float(1/np.mean(mu_f))}
    return Phi, info

# ============================================================
# P(k) measurement
# ============================================================
def meas_Pk(pos,N,L):
    rho=cic_dep(pos,N,L);d=rho-1;dk=fftn(d);V=L**3
    P3=np.abs(dk)**2*V/N**6
    kx=2*np.pi*fftfreq(N,d=L/N);A,B,C=np.meshgrid(kx,kx,kx,indexing='ij')
    K=np.sqrt(A**2+B**2+C**2)
    kf=2*np.pi/L;kny=np.pi*N/L;edges=np.arange(kf,kny,kf)
    nc=len(edges)-1;kc=np.zeros(nc);Pb=np.zeros(nc);ct=np.zeros(nc)
    Kf=K.ravel();Pf=P3.ravel()
    for i in range(nc):
        m=(Kf>=edges[i])&(Kf<edges[i+1])
        if np.any(m):kc[i]=np.mean(Kf[m]);Pb[i]=np.mean(Pf[m]);ct[i]=np.sum(m)
    ok=ct>0;kc=kc[ok];Pb=Pb[ok]
    W2=np.sinc(kc*L/(N*2*np.pi))**4
    return kc,Pb/np.maximum(W2,0.01)

# ============================================================
# N-body simulation
# ============================================================
def run(mode,Om,OL,pos0,vel0):
    print(f"\n{'='*60}\n  {mode}  Om={Om}\n{'='*60}")
    ai=1/(1+ZI);a_arr=np.logspace(np.log10(ai),0,NS+1)
    pos=pos0.copy();vel=vel0.copy()
    out={'mode':mode,'snaps':{},'md':[]}
    t0=time.time()

    for s in range(NS):
        a0=a_arr[s];a1=a_arr[s+1];am=.5*(a0+a1)
        Hm=100*np.sqrt(Om/am**3+OL);dt=(a1-a0)/(am*Hm)
        z_now=1/a0-1

        rho=cic_dep(pos,NG,L);delta=rho-1
        pf=1.5*Om*H0SQ/a0

        if mode=='DFD':
            Phi,mi=solve_MOND_EFE(delta,pf,NG,L,z_now,Om,OL,tol=5e-3,maxit=150,w0=0.05)
            mi['z']=float(z_now);mi['a']=float(a0)
            out['md'].append(mi)
        else:
            Phi=poisson(delta,pf,NG,L);mi=None

        gx,gy,gz=grad3(Phi,DX)
        Ax,Ay,Az=cic_int(-gx,-gy,-gz,pos,NG,L)

        fric=a0/a1;kick=dt/a0
        vel[:,0]=vel[:,0]*fric+Ax*kick
        vel[:,1]=vel[:,1]*fric+Ay*kick
        vel[:,2]=vel[:,2]*fric+Az*kick
        drift=dt/am
        pos=(pos+vel*drift)%L

        ze=1/a1-1
        for zo in ZOUT:
            if zo not in out['snaps']:
                dz=abs(ze-zo);dzs=abs(1/a1-1/a0)
                if dz<0.6*dzs or (zo==0 and s==NS-1):
                    k,P=meas_Pk(pos,NG,L)
                    s8=sig_R(k,P,8.0)
                    dr=np.std(cic_dep(pos,NG,L)-1)
                    sn={'z':float(ze),'k':k.tolist(),'Pk':P.tolist(),
                        's8':float(s8),'dr':float(dr)}
                    if mi:
                        for key in ['x_bar','mu_bg','x_eff_bar','mu_eff_bar','Geff_over_G','it','rel']:
                            sn[key]=mi[key]
                    out['snaps'][f'z{zo:.1f}']=sn
                    pr=f"  [{mode}] z={ze:.2f} s8={s8:.4f} dr={dr:.4f}"
                    if mi: pr+=f" xb={mi['x_bar']:.2f} mu={mi['mu_eff_bar']:.4f} G/Gn={mi['Geff_over_G']:.3f}"
                    print(pr)
        if s%50==0 and s>0:
            print(f"  [{mode}] step {s}/{NS} z={ze:.1f} ({time.time()-t0:.0f}s)")

    out['t']=time.time()-t0;print(f"  [{mode}] done {out['t']:.0f}s")
    return out

# ============================================================
# Main
# ============================================================
def main():
    print("="*70)
    print("  R5: DFD PM N-body — Nonlinear MOND with sigma_nabla Regulation")
    print("="*70)

    s8b=0.15; s8L=0.811

    print(f"\n--- Baryon ICs s8={s8b} ---")
    pb,vb=gen_ICs(Omega_b,Omega_Lb,s8b,seed=42)
    print(f"\n--- LCDM ICs s8={s8L} ---")
    pL,vL=gen_ICs(Omega_mL,Omega_LL,s8L,seed=42)

    R={}
    R['DFD']=run('DFD',Omega_b,Omega_Lb,pb.copy(),vb.copy())
    R['Newton']=run('Newton',Omega_b,Omega_Lb,pb.copy(),vb.copy())
    R['LCDM']=run('LCDM',Omega_mL,Omega_LL,pL.copy(),vL.copy())

    # ============================================================
    # Results
    # ============================================================
    print("\n"+"="*70+"\n  RESULTS\n"+"="*70)

    summary={'params':{'NG':NG,'L':L,'zi':ZI,'Ns':NS,'a0':float(a0_code),
                       'c_code':float(c_code),
                       's8b':s8b,'s8L':s8L},'R':{}}

    for m in ['DFD','Newton','LCDM']:
        r=R[m];print(f"\n  {m} ({r['t']:.0f}s)")
        summary['R'][m]={'t':r['t'],'snaps':{}}
        for zk in sorted(r['snaps'].keys()):
            sn=r['snaps'][zk]
            ln=f"    {zk}: s8={sn['s8']:.4f} dr={sn['dr']:.4f}"
            if 'x_bar' in sn: ln+=f" xb={sn['x_bar']:.2f} mu={sn['mu_eff_bar']:.4f} G/Gn={sn['Geff_over_G']:.3f}"
            print(ln)
            summary['R'][m]['snaps'][zk]={k:sn[k] for k in sn}

    # sigma_8 table
    print("\n  sigma_8 evolution:")
    print(f"    {'z':>6} {'DFD':>10} {'Newton':>10} {'LCDM':>10} {'DFD/Newt':>10} {'DFD/LCDM':>10}")
    for zk in sorted(R['DFD']['snaps'].keys()):
        sd=R['DFD']['snaps'].get(zk,{})
        sn=R['Newton']['snaps'].get(zk,{})
        sl=R['LCDM']['snaps'].get(zk,{})
        s8d=sd.get('s8',0);s8n=sn.get('s8',0);s8l=sl.get('s8',0)
        r1=s8d/s8n if s8n>0 else 0;r2=s8d/s8l if s8l>0 else 0
        print(f"    {zk:>6} {s8d:10.4f} {s8n:10.4f} {s8l:10.4f} {r1:10.4f} {r2:10.4f}")

    # P(k) ratios
    def S(m,z): return R[m]['snaps'].get(z)
    print("\n  P(k) ratios at z=0:")
    print(f"    {'k':>8} {'DFD/LCDM':>12} {'DFD/Newton':>12}")
    sd,sN,sL=S('DFD','z0.0'),S('Newton','z0.0'),S('LCDM','z0.0')
    if sd and sN and sL:
        kd,Pd=np.array(sd['k']),np.array(sd['Pk'])
        kn,Pn=np.array(sN['k']),np.array(sN['Pk'])
        kl,Pl=np.array(sL['k']),np.array(sL['Pk'])
        for kv in [0.01,0.02,0.05,0.1,0.2,0.5]:
            i=np.argmin(np.abs(kd-kv))
            rDL=Pd[i]/(np.interp(kd[i],kl,Pl)+1e-30)
            rDN=Pd[i]/(np.interp(kd[i],kn,Pn)+1e-30)
            print(f"    {kd[i]:8.3f} {rDL:12.4f} {rDN:12.4f}")
        summary['ratios_z0']={'k':kd.tolist(),
            'DFD_LCDM':(Pd/(np.interp(kd,kl,Pl)+1e-30)).tolist(),
            'DFD_Newton':(Pd/(np.interp(kd,kn,Pn)+1e-30)).tolist()}

    # MOND regulation evolution
    if R['DFD']['md']:
        print("\n  MOND self-regulation evolution:")
        print(f"    {'z':>6} {'x_bar':>8} {'mu_bg':>8} {'mu_eff':>8} {'G/Gn':>8} {'res':>10} {'it':>4}")
        dg=R['DFD']['md']; nd=len(dg)
        si=np.linspace(0,nd-1,min(15,nd)).astype(int)
        reg=[]
        for i in si:
            d=dg[i]
            reg.append({k:d[k] for k in d})
            print(f"    {d['z']:6.1f} {d['x_bar']:8.3f} {d['mu_bg']:8.4f} "
                  f"{d['mu_eff_bar']:8.4f} {d['Geff_over_G']:8.3f} "
                  f"{d['rel']:10.2e} {d['it']:4d}")
        summary['regulation']=reg

    op=os.path.join(os.path.dirname(os.path.abspath(__file__)),'R5_nbody_data.json')
    with open(op,'w') as f: json.dump(summary,f,indent=2,default=str)
    print(f"\n  Saved {op}")
    return summary

if __name__=='__main__':
    main()
