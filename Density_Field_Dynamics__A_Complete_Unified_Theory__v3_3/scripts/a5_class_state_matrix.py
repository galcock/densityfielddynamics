#!/usr/bin/env python3
"""Reproduces normalized A5 class-state matrix elements <C_i|T|C_j>.
Outputs the key identity→order-3 amplitude = 2/sqrt(20) = 1/sqrt(5).
"""
import math, collections, numpy as np

def perm_from_cycles(cycles):
    p=list(range(1,6))
    for cyc in cycles:
        k=len(cyc)
        for i in range(k):
            p[cyc[i]-1]=cyc[(i+1)%k]
    return tuple(p)

def compose(p,q):
    return tuple(p[i-1] for i in q)

def inv(p):
    r=[0]*5
    for i,a in enumerate(p, start=1):
        r[a-1]=i
    return tuple(r)

e=tuple(range(1,6))
a=perm_from_cycles([(1,2,3)])
b=perm_from_cycles([(1,2,3,4,5)])
S=[a,inv(a),b,inv(b)]

# generate A5
G=[e]; seen={e}; q=collections.deque([e])
while q:
    g=q.popleft()
    for s in S:
        h=compose(g,s)
        if h not in seen:
            seen.add(h); G.append(h); q.append(h)
assert len(G)==60
idx={g:i for i,g in enumerate(G)}
def mul_idx(i,j): return idx[compose(G[i],G[j])]
inv_idx=[idx[inv(g)] for g in G]

def order_idx(i,limit=200):
    x=idx[e]
    for k in range(1,limit+1):
        x=mul_idx(x,i)
        if x==idx[e]: return k
    return None
orders=[order_idx(i) for i in range(60)]

# conjugacy classes
unvisited=set(range(60))
classes=[]
while unvisited:
    g=next(iter(unvisited))
    C=set()
    for h in range(60):
        C.add(mul_idx(mul_idx(h,g), inv_idx[h]))
    for x in C: unvisited.discard(x)
    classes.append(sorted(C))
classes.sort(key=lambda C:(len(C),orders[C[0]]))

class_sizes=[len(C) for C in classes]
class_orders=[orders[C[0]] for C in classes]

# Cayley operator (right mult)
gen_idx=[idx[s] for s in S]
T=np.zeros((60,60))
for i in range(60):
    for s in gen_idx:
        j=mul_idx(i,s)
        T[j,i]+=1

# normalized class states
class_states=[]
for C in classes:
    v=np.zeros(60)
    for g in C: v[g]=1
    v=v/math.sqrt(len(C))
    class_states.append(v)

T_class=np.array([[class_states[i]@T@class_states[j] for j in range(len(classes))]
                  for i in range(len(classes))])

# identify order-3 and identity classes
C3_idx=[i for i,(sz,ordr) in enumerate(zip(class_sizes,class_orders)) if sz==20 and ordr==3][0]
C0_idx=[i for i,(sz,ordr) in enumerate(zip(class_sizes,class_orders)) if sz==1 and ordr==1][0]

amp=T_class[C3_idx,C0_idx]

np.set_printoptions(precision=6, suppress=True)
print("|A5| =", len(G))
print("Conjugacy classes (size, order):", list(zip(class_sizes,class_orders)))
print("Key amplitude <C3|T|e> =", amp)
print("2/sqrt(20) =", 2/math.sqrt(20))
print("1/sqrt(5)  =", 1/math.sqrt(5))
print("\nT_class =\n", T_class)
