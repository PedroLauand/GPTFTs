import numpy as np, itertools, time, sys
from numpy.linalg import matrix_power as mpow
from scipy.optimize import linprog, minimize
np.set_printoptions(precision=4, suppress=True, linewidth=150)
rng=np.random.default_rng(0)

# ---------- Herm_2, Herm_4 with orthonormal Pauli coordinates ----------
s0=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]],complex); s3=np.diag([1,-1]).astype(complex)
P=[s0,s1,s2,s3]
B1=[p/np.sqrt(2) for p in P]
B2=[np.kron(p,q)/2 for p in P for q in P]
co1=lambda X: np.array([np.real(np.trace(X@b)) for b in B1])
co2=lambda X: np.array([np.real(np.trace(X@b)) for b in B2])
op1=lambda x: sum(xi*b for xi,b in zip(x,B1))
op2=lambda x: sum(xi*b for xi,b in zip(x,B2))

# ---------- OST ----------
r=2**0.25
R=np.diag([np.exp(-1j*np.pi/8),np.exp(1j*np.pi/8)])
st=lambda v: 0.5*(s0+v[0]*s1+v[1]*s2+v[2]*s3)
Om=[st([r,0,0]),st([-r,0,0]),st([0,r,0]),st([0,-r,0]),st([0,0,1]),st([0,0,-1])]
Ef=[R@w@R.conj().T for w in Om]
bell=np.array([1,0,0,1],complex)/np.sqrt(2)
Phi=[]
for mu in range(4):
    for m in (1,3,5,7):
        U=P[mu]@mpow(R,m); v=np.kron(U.conj().T,s0)@bell; S=np.outer(v,v.conj())
        if not any(np.allclose(S,T) for T in Phi): Phi.append(S)
gensD2=[np.kron(a,b) for a in Om for b in Om]+Phi
gensP2=[np.kron(a,b) for a in Ef for b in Ef]+Phi
GD=np.array([co2(g) for g in gensD2]).T; GP=np.array([co2(g) for g in gensP2]).T
def slackD1(X):
    t=np.real(np.trace(X)); v=np.real([np.trace(X@s1),np.trace(X@s2),np.trace(X@s3)])
    return t-(abs(v[0])/r+abs(v[1])/r+abs(v[2]))
def slackP1(X): return slackD1(R.conj().T@X@R)
def l1dist(x,G):
    n=G.shape[1]; d=G.shape[0]
    c=np.r_[np.zeros(n),np.ones(2*d)]; A=np.c_[G,np.eye(d),-np.eye(d)]
    res=linprog(c,A_eq=A,b_eq=x,bounds=[(0,None)]*(n+2*d),method='highs'); return res.fun
def inD2(X): return l1dist(co2(X),GD)
def inP2(X): return l1dist(co2(X),GP)

print("== OST sanity ==")
print("distinct Phi states:",len(Phi))
print("min pairing Phi vs product effects:",min(np.real(np.trace(f@e)) for f in Phi for e in gensP2[:36]))
bell0=np.outer(bell,bell.conj())
print("untwisted Bell vs product effects (min):",min(np.real(np.trace(bell0@e)) for e in gensP2[:36]))
print("l1dist(untwisted Bell, D2) =",inD2(bell0), "  l1dist(Phi_01, D2) =",inD2(Phi[0]))
# snake with eta=4*Phi_01 (cup), eps=Phi_01 (cap): check transfer = identity on Herm_2
cup=4*Phi[0]; cap=Phi[0]
def snake(X):  # (cap_{12} ⊗ id_3)(X_1 ⊗ cup_{23})
    T=np.kron(X,cup).reshape(2,2,2,2,2,2)  # indices (1,2,3),(1',2',3')
    C=cap.reshape(2,2,2,2)
    return np.einsum('abcdef,dead->cf',T,C)  # wait computed below properly
def snake2(X):
    T=np.kron(X,cup)  # 8x8 on H1⊗H2⊗H3
    Cf=np.kron(cap,s0)  # cap on 12 as operator, tensor identity on 3
    Y=Cf@T  # then partial trace over 1,2
    Y=Y.reshape(4,2,4,2); return np.einsum('aiaj->ij',Y)
for X in Om[:3]:
    print("snake(X)-X norm:",np.linalg.norm(snake2(X)-X))

# ---------- doubled qubit theories D(Z) ----------
def doubled(W,th):
    V=sum(th[i]**-0.5*np.outer(np.kron(W[:,i],W[:,i]),W[:,i].conj()) for i in range(2))
    eta=sum(th[i]**0.5*W[:,i] for i in range(2))
    return (lambda X: V.conj().T@X@V), (lambda X: V@X@V.conj().T), np.outer(eta,eta.conj())
def basis(alpha,psi):
    a=np.array([np.cos(alpha/2),np.exp(1j*psi)*np.sin(alpha/2)])
    b=np.array([np.sin(alpha/2),-np.exp(1j*psi)*np.cos(alpha/2)])
    return np.c_[a,b], np.array([np.cos(alpha/2)**2,np.sin(alpha/2)**2])
def rel(s,X): return s/(np.linalg.norm(X)+1e-15)
def cheap_doubled(mu,De,E):
    t1=min(rel(slackD1(mu(g)),mu(g)) for g in gensD2)   # pants on states
    t2=min(rel(slackP1(mu(f)),mu(f)) for f in gensP2)   # copants^* on effects (= mu for dagger theories)
    t5=min(rel(slackD1(E),E),rel(slackP1(E),E))
    return t1,t2,t5
print("\n== doubled qubit scan (unit forced to |0><0|) ==")
best=(-9,None)
rows=[]
for alpha in np.linspace(0.02,np.pi-0.02,90):
    for psi in np.linspace(0,2*np.pi,96,endpoint=False):
        W,th=basis(alpha,psi); mu,De,E=doubled(W,th)
        t1,t2,t5=cheap_doubled(mu,De,E)
        rows.append((alpha,psi,t1,t2,t5))
        if min(t1,t2,t5)>best[0]: best=(min(t1,t2,t5),(alpha,psi,t1,t2,t5))
print("best min-slack over grid (>=0 would mean pass):",best)
# pants only, best
bp=max(rows,key=lambda q:q[2]); print("best pants slack alone: alpha=%.3f psi=%.3f t1=%.4f"%(bp[0],bp[1],bp[2]))
# cup-compatible family psi = pi/8 + k pi/4
print("cup-compatible family (psi=22.5°+k45°), pants slack vs alpha:")
for psi in [np.pi/8+k*np.pi/4 for k in range(4)]:
    vals=[]
    for alpha in np.linspace(0.05,np.pi-0.05,40):
        W,th=basis(alpha,psi); mu,De,E=doubled(W,th); t1,t2,t5=cheap_doubled(mu,De,E); vals.append((alpha,t1,t2))
    a,t1,t2=max(vals,key=lambda q:q[1]); print("  psi=%.1f°: best pants slack %.4f at alpha=%.2f (t2=%.4f)"%(np.degrees(psi),t1,a,t2))
# which generator fails at the best point, and the copants LP there
alpha,psi=best[1][0],best[1][1]; W,th=basis(alpha,psi); mu,De,E=doubled(W,th)
worst=min(range(len(gensD2)),key=lambda i: rel(slackD1(mu(gensD2[i])),mu(gensD2[i])))
print("worst generator index at best point:",worst,"(0-35 product states, 36+ Phi)  slack:",slackD1(mu(gensD2[worst])))
print("copants LP l1dist(Delta(omega),D2) at best point:",[round(inD2(De(w)),4) for w in Om])
print("cup = Delta(eta): l1dist to D2:",round(inD2(De(E)),4))
# analytic check: equatorial basis, x+ (x) x-
W,th=basis(np.pi/2,0.0); mu,De,E=doubled(W,th)
print("equatorial basis psi=0: mu(x+ (x) x-) =",np.round(mu(np.kron(Om[0],Om[1])),4).tolist(), " expected (1-r^2)/4*I =",(1-r**2)/4)

# ---------- validation: the same doubled theory against the qubit's PSD cones ----------
print("\n== validation: doubled theory vs PSD cones (should all be >= 0) ==")
W,th=basis(1.1,0.7); mu,De,E=doubled(W,th)
mineig=lambda X: np.linalg.eigvalsh((X+X.conj().T)/2).min()
psd2=[np.kron(a,b) for a in Om for b in Om if mineig(np.kron(a,b))>-1e-9]  # only PSD products
print("pants on PSD products/Phi min eig:",min(mineig(mu(g)) for g in psd2+Phi))
print("copants on PSD states min eig:",min(mineig(De(w)) for w in Om if mineig(w)>-1e-9))

# ---------- admissible Frobenius forms (caps) ----------
print("\n== admissible caps: symmetric cone isomorphisms D1 -> P1 that are OST effects with inverse an OST state ==")
lens=np.array([r,r,1.0]); c45=np.cos(np.pi/4); Rot=np.array([[c45,-c45,0],[c45,c45,0],[0,0,1]])
caps=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1,-1],repeat=3):
        L=np.zeros((3,3))
        for k in range(3): L[perm[k],k]=signs[k]*lens[perm[k]]/lens[k]
        B3=Rot@L
        if not np.allclose(B3,B3.T): continue
        Bm=np.eye(4); Bm[1:,1:]=B3          # bilinear form in orthonormal coords: beta(x,y)=x^T Bm y
        F=op2(Bm.flatten()); Ginv=np.linalg.inv(Bm); Gop=op2(Ginv.flatten())
        dP=l1dist(Bm.flatten(),GP); dD=l1dist(Ginv.flatten(),GD)
        caps.append((perm,signs,dP,dD))
        print(" perm",perm,"signs",signs," beta in P2: l1dist=%.2e  inverse in D2: l1dist=%.2e"%(dP,dD), " <-- admissible" if dP<1e-7 and dD<1e-7 else "")

# ---------- general semisimple commutative Frobenius algebras on R^4 ----------
print("\n== general search over semisimple Frobenius algebras on Herm_2 ==")
def algebra(kind,M,th,ws):
    n=4; Minv=np.linalg.inv(M); prod=np.zeros((n,n,n)); slots=[]; idx=0
    for s in kind:
        slots.append((s,idx)); idx+= 1 if s=='R' else 2
    one=np.zeros(n); ec=np.zeros(n); ri=ci=0
    for s,i in slots:
        if s=='R': prod[i,i,i]=1; one[i]=1; ec[i]=th[ri]; ri+=1
        else:
            u,v=i,i+1; prod[u,u,u]=1; prod[u,v,v]=1; prod[v,u,v]=1; prod[v,v,u]=-1
            one[u]=1; ec[u]=ws[ci].real; ec[v]=ws[ci].imag; ci+=1
    G=np.einsum('abc,c->ab',prod,ec); Ginv=np.linalg.inv(G)
    K=np.kron(M,M); Kinv=np.linalg.inv(K)
    mu=M@prod.reshape(n*n,n).T@Kinv
    T=np.einsum('cad,ab->cdb',prod,Ginv)
    De=K@T.reshape(n,n*n).T@Minv
    return mu,De,M@one,Minv.T@ec
def check_frobenius(mu,De,eta,eps):
    I4=np.eye(4)
    assoc=np.linalg.norm(mu@np.kron(mu,I4)-mu@np.kron(I4,mu))
    unit=np.linalg.norm(mu@np.kron(eta[:,None],I4)-I4)
    frob=np.linalg.norm(np.kron(mu,I4)@np.kron(I4,De)-De@mu)
    coun=np.linalg.norm(np.kron(eps[None,:],I4)@De-I4)
    comm=np.linalg.norm(mu-mu@np.kron(I4,I4)[[4*i+j for j in range(4) for i in range(4)],:])
    return assoc,unit,frob,coun,comm
# validate with the doubled qubit expressed in this parametrisation
W,th=basis(1.1,0.7); a,b=W[:,0],W[:,1]
Pab=np.outer(a,b.conj())+np.outer(b,a.conj()); Qab=1j*(np.outer(a,b.conj())-np.outer(b,a.conj()))
M=np.c_[co1(np.outer(a,a.conj())),co1(np.outer(b,b.conj())),co1(Pab),co1(Qab)]
mu,De,eta,eps=algebra(['R','R','C'],M,th,[2*np.sqrt(th[0]*th[1])+0j])
print("Frobenius identities (assoc,unit,frob,counit,comm):",np.round(check_frobenius(mu,De,eta,eps),10))
muD,DeD,E=doubled(W,th)
x=co2(gensD2[7]); print("general-parametrisation mu vs V^dag X V:",np.linalg.norm(op1(mu@x)-muD(gensD2[7])), " Delta:",np.linalg.norm(op2(De@co1(Om[2]))-DeD(Om[2])), " eta:",np.linalg.norm(op1(eta)-E), " eps:",np.linalg.norm(op1(eps)-E))
# random algebra identities
Mr=rng.normal(size=(4,4)); mu,De,eta,eps=algebra(['R','R','C'],Mr,[0.7,1.3],[0.4-0.9j]); print("random R2+C identities:",np.round(check_frobenius(mu,De,eta,eps),10))
mu,De,eta,eps=algebra(['C','C'],Mr,[],[0.4-0.9j,1.1+0.2j]); print("random C+C identities:",np.round(check_frobenius(mu,De,eta,eps),10))

GD2=[co2(g) for g in gensD2]; GP2=[co2(g) for g in gensP2]
def violation(kind,M,th,ws,detail=False):
    try: mu,De,eta,eps=algebra(kind,M,th,ws)
    except np.linalg.LinAlgError: return 1e3
    v=0.0; parts=[]
    t1=min(rel(slackD1(op1(mu@x)),op1(mu@x)) for x in GD2)          # pants: states
    t2=min(rel(slackP1(op1(De.T@x)),op1(De.T@x)) for x in GP2)      # copants^*: effects
    t5a=rel(slackD1(op1(eta)),op1(eta)); t5b=rel(slackP1(op1(eps)),op1(eps))
    for t in (t1,t2,t5a,t5b): v+=max(0,-t)
    if detail: return t1,t2,t5a,t5b
    return v
def unpack(kind,p):
    M=p[:16].reshape(4,4); k=kind.count('R'); m=kind.count('C')
    th=np.exp(p[16:16+k]); ws=[p[16+k+2*i]+1j*p[16+k+2*i+1] for i in range(m)]
    return M,th,ws
def run_search(kind,nstart,maxiter,budget):
    t0=time.time(); bestv=1e9; bestp=None; k=kind.count('R'); m=kind.count('C')
    for s in range(nstart):
        if time.time()-t0>budget: break
        p0=np.r_[rng.normal(size=16),rng.normal(size=k)*0.5,rng.normal(size=2*m)]
        f=lambda p: violation(kind,*unpack(kind,p))
        res=minimize(f,p0,method='Nelder-Mead',options={'maxiter':maxiter,'xatol':1e-6,'fatol':1e-9})
        if res.fun<bestv: bestv=res.fun; bestp=res.x
    return bestv,bestp,s+1
for kind in (['R','R','R','R'],['R','R','C'],['C','C']):
    bestv,bestp,ns=run_search(kind,400,3000,110)
    M,th,ws=unpack(kind,bestp)
    print(kind,"starts:",ns," best total violation: %.4e"%bestv," slacks (pants,copants*,eta,eps):",np.round(violation(kind,M,th,ws,True),4))
