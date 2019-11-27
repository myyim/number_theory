import math

def nCr(n,r):
    """nCr(n,r) returns n choose r"""
    if n>=r:
        return math.factorial(n)/math.factorial(r)/math.factorial(n-r)
    else:
        return 0

def Stirling2(n,k):
    """Stirling numbers of the second kind S(n,k)"""
    num = 0
    for i in range(k+1):
        num += (-1)**i*nCr(k,i)*(k-i)**n
    return num/math.factorial(k)

def PolyBernoulli(n,k):
    """Poly-Bernoulli number B^(-k)_n"""
    num = 0
    for m in range(n+1):
        num += (-1)**(m+n)*math.factorial(m)*Stirling2(n,m)*(m+1)**k
    return num
