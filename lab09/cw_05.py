lista=[9,7,4,6,3,1,0]
lista1=[]
for j in range(len(lista)):
    for i in range (len(lista)):
        if i+1<len(lista):
            min = lista[i] if lista[i] < lista[i+1] else lista[i+1]
    lista1.append(min)
    lista.pop(lista.index(min))


print(lista1)