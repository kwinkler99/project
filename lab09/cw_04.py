lista = [9,7,4,6,3,1,0]



for n, i in enumerate(lista):
    if n>0:
        j = n-1
        while lista[j]<i and j >= 0:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = i


print(lista)