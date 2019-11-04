n=int(input("Podaj liczbe n: "))
lista=[]
for i in range(n):
    m=int(input("podaj liczbe m: "))
    lista.append(m)

print(lista[::-1])