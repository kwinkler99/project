def wyraz(n):
    if n==1: return 1
    elif n == 2: return 1
    else: return wyraz(n-1) + wyraz(n-2)


print(wyraz(10))