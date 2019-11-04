n=int(input("Podaj liczbe: "))
lista=[]
lista1=[]
mnozenie=[]

for i in range(n):
    m=int(input("Podaj liczbe m: "))
    lista.append(m)
for j in range(n):
    m=int(input("Podaj liczbe m1: "))
    lista1.append(m)

for k in range(n):

    mnozenie.append(lista[k]*lista1[k])


print(lista)
print(lista1)
print(mnozenie)
