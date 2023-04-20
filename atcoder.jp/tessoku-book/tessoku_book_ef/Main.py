# Find inversion number in O(nlogn)
# Bucket + RSQ

class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])# type: ignore
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)# type: ignore
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)# type: ignore
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):# type: ignore
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):# type: ignore
                        sm=self.op(sm,self.d[l])# type: ignore
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])# type: ignore
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<=self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):# type: ignore
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):# type: ignore
                        sm=self.op(self.d[r],sm)# type: ignore
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)# type: ignore
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1]) # type: ignore
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))
Bucket = [0]*(N)
Z = segtree(Bucket, lambda x, y: x+y, 0)
cnt = 0

for item in A:
    cnt += Z.prod(item, N)
    Z.set(item, 1)
    # 自分より大きい数字がもう出ていたら、転倒数とカウントする
    
print(cnt)