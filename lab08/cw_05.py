def newton(n,k):
    if n==k or k==0: return 1
    else: return newton(n-1,k)+newton(n-1,k-1)

print(newton(5,2))