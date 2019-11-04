lista=[]
n=int(input("Podaj liczbe: "))
lista.append(n)

while n!=0:
    n = int(input("Podaj liczbe: "))
    lista.append(n)

print(lista)
print(lista[::2])
sumalisty=sum(lista[::2])
print(sumalisty)