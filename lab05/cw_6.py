n=str(input("Podaj napis: "))
lista=[n]
lista1=[]
while n:
    n = str(input("Podaj napis: "))
    if n:
        lista.append(n)

print(lista)

for i in range(len(lista)):
    krotka=(lista[i],len(lista[i]))
    lista1.append(krotka)

print(lista1)