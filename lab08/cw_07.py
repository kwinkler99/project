def max(lista,n):
    if lista[0] > n: return 0
    elif len(lista)==1 and lista[0]<n: return 1
    elif len(lista)==1: return 0
    else: return max(lista[1:],n)

tablica=[1,3,4,5,6,7,11,9,3]
print(max(tablica,20))