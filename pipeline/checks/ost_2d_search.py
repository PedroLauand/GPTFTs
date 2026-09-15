import numpy as np, itertools, time
from numpy.linalg import matrix_power as mpow
from scipy.optimize import linprog, minimize
np.set_printoptions(precision=4, suppress=True, linewidth=150)
rng=np.random.default_rng(1)
s0=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]],complex); s3=np.diag([1,-1]).astype(complex)
P=[s0,s1,s2,s3]; B1=[p/np.sqrt(2) for p in P]; B2=[np.kron(p,q)/2 for p in P for q in P]
co1=lambda X: np.array([np.real(np.trace(X@b)) for b in B1]); co2=lambda X: np.array([np.real(np.trace(X@b)) for b in B2])
op1=lambda x: sum(xi*b for xi,b in zip(x,B1))
r=2**0.25; R=np.diag([np.exp(-1j*np.pi/8),np.exp(1j*np.pi/8)])
st=lambda v: 0.5*(s0+v[0]*s1+v[1]*s2+v[2]*s3)
Om=[st([r,0,0]),st([-r,0,0]),st([0,r,0]),st([0,-r,0]),st([0,0,1]),st([0,0,-1])]
Ef=[R@w@R.conj().T for w in Om]
bell=np.array([1,0,0,1],complex)/np.sqrt(2); Phi=[]
for mu_ in range(4):
    for m in (1,3,5,7):
        U=P[mu_]@mpow(R,m); v=np.kron(U.conj().T,s0)@bell; S=np.outer(v,v.conj())
        if not any(np.allclose(S,T) for T in Phi): Phi.append(S)
gensD2=[np.kron(a,b) for a in Om for b in Om]+Phi; gensP2=[np.kron(a,b) for a in Ef for b in Ef]+Phi
GD=np.array([co2(g) for g in gensD2]).T; GP=np.array([co2(g) for b in [0] for g in gensP2]).T
XD=GD.copy(); XP=GP.copy()   # columns: coordinates of generators
def l1dist(x,G):
    n=G.shape[1]; d=G.shape[0]; c=np.r_[np.zeros(n),np.ones(2*d)]; A=np.c_[G,np.eye(d),-np.eye(d)]
    return linprog(c,A_eq=A,b_eq=x,bounds=[(0,None)]*(n+2*d),method='highs').fun
c45=np.cos(np.pi/4)
def slD1(Y):   # Y: 4 x N orthonormal coords; relative slack of D1 membership per column
    t=Y[0]; a=abs(Y[1])/r+abs(Y[2])/r+abs(Y[3]); return (t-a)/(np.linalg.norm(Y,axis=0)+1e-15)
def slP1(Y):
    Z=Y.copy(); Z[1]=c45*Y[1]+c45*Y[2]; Z[2]=-c45*Y[1]+c45*Y[2]; return slD1(Z)

# ---- 1. doubled theories: alpha -> 0 trend and the handle element ----
def basis(alpha,psi):
    a=np.array([np.cos(alpha/2),np.exp(1j*psi)*np.sin(alpha/2)]); b=np.array([np.sin(alpha/2),-np.exp(1j*psi)*np.cos(alpha/2)])
    return np.c_[a,b], np.array([np.cos(alpha/2)**2,np.sin(alpha/2)**2])
def doubled(W,th):
    V=sum(th[i]**-0.5*np.outer(np.kron(W[:,i],W[:,i]),W[:,i].conj()) for i in range(2))
    return V
print("== doubled theories: pants slack as alpha -> 0 (psi=0 and psi=22.5 deg) ==")
for psi in (0.0, np.pi/8):
    for alpha in (0.3,0.1,0.03,0.01,0.003,0.001):
        W,th=basis(alpha,psi); V=doubled(W,th)
        Y=np.array([co1(V.conj().T@g@V) for g in gensD2]).T
        s=slD1(Y); i=np.argmin(s)
        print("  psi=%.1f° alpha=%.3f  min pants slack %.4f (generator %d)"%(np.degrees(psi),alpha,s.min(),i))
print("handle element h = mu(cup) for the cup-compatible family (psi=22.5°): is |h><h| in D1?")
for alpha in np.linspace(0.3,np.pi-0.3,7):
    W,th=basis(alpha,np.pi/8); V=doubled(W,th); cup=V@np.outer(*(2*[W[:,0]*0+np.array([1,0],complex)]))@V.conj().T
    eta=np.array([1,0],complex); cup=V@np.outer(eta,eta.conj())@V.conj().T; h=V.conj().T@cup@V
    print("  alpha=%.2f  slack(h)=%.4f"%(alpha,slD1(co1(h)[:,None])[0]))

# ---- 2. general semisimple algebras with the Frobenius form fixed to the Bell cap Phi_{0,1} ----
# Bell cap as bilinear form in orthonormal coords: beta(x,y) = tr(Phi01 (X⊗Y)) * 2 -> matrix Bm
F=co2(Phi[0])*2; Bm=F.reshape(4,4); Bm=(Bm+Bm.T)/2
print("\nBell-cap form matrix (orthonormal Pauli coords), eigenvalues:",np.linalg.eigvalsh(Bm))
def bdot(x,y): return x@Bm@y
def struct(kind,vecs):
    """vecs: list of 4 basis vectors in orthonormal coords: for 'R' one idempotent, for 'C' the pair (1_C, j).
       returns mu (4x16), De (16x4), eta (4), eps (4)"""
    M=np.array(vecs).T; Minv=np.linalg.inv(M); n=4; prod=np.zeros((n,n,n)); one=np.zeros(n); idx=0
    for s in kind:
        if s=='R': prod[idx,idx,idx]=1; one[idx]=1; idx+=1
        else:
            u,v=idx,idx+1; prod[u,u,u]=1; prod[u,v,v]=1; prod[v,u,v]=1; prod[v,v,u]=-1; one[u]=1; idx+=2
    eta=M@one; eps=Bm@eta              # eps = beta(eta, .)
    ec=M.T@eps                          # eps in M-basis
    G=np.einsum('abc,c->ab',prod,ec); Ginv=np.linalg.inv(G)
    K=np.kron(M,M); Kinv=np.linalg.inv(K)
    mu=M@prod.reshape(n*n,n).T@Kinv
    T=np.einsum('cad,ab->cdb',prod,Ginv); De=K@T.reshape(n,n*n).T@Minv
    return mu,De,eta,eps,G
def frob_ok(mu,De,eta,eps):
    I4=np.eye(4)
    return max(np.linalg.norm(mu@np.kron(mu,I4)-mu@np.kron(I4,mu)), np.linalg.norm(mu@np.kron(eta[:,None],I4)-I4),
               np.linalg.norm(np.kron(mu,I4)@np.kron(I4,De)-De@mu), np.linalg.norm(np.kron(eps[None,:],I4)@De-I4))
def form_ok(mu,eps):   # beta(x,y) = eps(mu(x⊗y)) must equal Bm
    Bt=np.array([[eps@mu@np.kron(np.eye(4)[i],np.eye(4)[j]) for j in range(4)] for i in range(4)]); return np.linalg.norm(Bt-Bm)
def borth_complement(vs):
    # basis of the beta-orthogonal complement of span(vs)
    A=np.array([Bm@v for v in vs]); _,_,Vt=np.linalg.svd(A); return Vt[len(vs):]
def build(kind,p):
    """p: parameter vector. Constructs beta-orthogonal decomposition. Returns vecs or None."""
    if kind=='RRC':
        p1=p[0:4]; q=p[4:8]
        if bdot(p1,p1)<=1e-9: return None
        p2=q-bdot(p1,q)/bdot(p1,p1)*p1
        if bdot(p2,p2)<=1e-9: return None
        C=borth_complement([p1,p2])            # 2 vectors spanning Pi
        Gc=np.array([[bdot(a,b) for b in C] for a in C]); w,U=np.linalg.eigh(Gc)
        if not (w[0]<0<w[1]): return None
        up=(C.T@U[:,1])/np.sqrt(w[1]); um=(C.T@U[:,0])/np.sqrt(-w[0])     # beta(up,up)=1, beta(um,um)=-1
        one=p[8]*up+p[9]*um
        s1=p[10]; s2=np.sqrt(s1**2+1)*np.sign(p[11]+1e-12)
        # J in (up,um) coords: [[s1,s2],[-s2,-s1]] ; j = J(one)
        x,y=p[8],p[9]; jx=s1*x+s2*y; jy=-s2*x-s1*y; j=jx*up+jy*um
        return [p1,p2,one,j]
    if kind=='RRRR':
        p1=p[0:4]
        if bdot(p1,p1)<=1e-9: return None
        q=p[4:8]; p2=q-bdot(p1,q)/bdot(p1,p1)*p1
        if bdot(p2,p2)<=1e-9: return None
        q=p[8:12]; p3=q-bdot(p1,q)/bdot(p1,p1)*p1-bdot(p2,q)/bdot(p2,p2)*p2
        if bdot(p3,p3)<=1e-9: return None
        C=borth_complement([p1,p2,p3]); p4=C[0]*p[12]
        if bdot(p4,p4)>=-1e-9: return None
        return [p1,p2,p3,p4]
def tests(kind,vecs):
    mu,De,eta,eps,G=struct(kind,vecs)
    Y1=mu@XD; Y2=De.T@XP
    t1=slD1(Y1).min(); t2=slP1(Y2).min()
    t5a=slD1(eta[:,None])[0]; t5b=slP1(eps[:,None])[0]
    # handle element and twisted handles are covered by t1 (Phi's are among the D2 generators)
    return np.array([t1,t2,t5a,t5b]),(mu,De,eta,eps)
def viol(kind,p):
    vecs=build(kind,p)
    if vecs is None: return 10.0
    try: t,_=tests(kind,vecs)
    except np.linalg.LinAlgError: return 10.0
    return float(np.sum(np.maximum(0,-t)))
# sanity: random RRC structure satisfies Frobenius identities and has form Bm
for kind,npar in (('RRC',12),('RRRR',13)):
    for _ in range(50):
        p=rng.normal(size=npar); v=build(kind,p)
        if v is not None: break
    mu,De,eta,eps,G=struct(kind,v); print(kind,"identities:",round(frob_ok(mu,De,eta,eps),10)," form==Bell cap:",round(form_ok(mu,eps),10)," Gram diag:",np.round(np.diag(G),3))
print("\n== search: total violation (0 = a 2d TFT in OST). states-side pants t1, effects-side copants* t2, unit t5a, counit t5b ==")
for kind,npar,budget in (('RRC',12,150),('RRRR',13,150)):
    t0=time.time(); best=(1e9,None); ns=0
    while time.time()-t0<budget:
        p0=rng.normal(size=npar)*rng.choice([0.5,1,2])
        if build(kind,p0) is None: continue
        res=minimize(lambda p: viol(kind,p),p0,method='Nelder-Mead',options={'maxiter':1500,'xatol':1e-7,'fatol':1e-10})
        ns+=1
        if res.fun<best[0]: best=(res.fun,res.x)
    t,(mu,De,eta,eps)=tests(kind,build(kind,best[1]))
    print(kind,"starts:",ns," best violation: %.4e"%best[0]," slacks:",np.round(t,4))
    # at the best point: which D2 generators break the pants; LP checks of copants
    Y1=mu@XD; s=slD1(Y1); print("   pants slack per generator class: products min %.3f, Phi min %.3f"%(s[:36].min(),s[36:].min()))
    print("   copants LP l1dist(Delta(omega),D2):",[round(l1dist(De@co1(w),GD),3) for w in Om])
    print("   eta coords:",np.round(eta,3)," Gram diag (theta's / a):",np.round(np.diag(struct(kind,build(kind,best[1]))[4]),3))
