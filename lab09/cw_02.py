lista = [6,5,4,2,3,1,0]

n = len(lista)

for i in range(n-1, 0,-1):
    for j in range(i):
        if lista[j]<lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)