n=int(input("Podaj liczbe: "))
lista=[]

for i in range(n):
    m=int(input("Podaj liczbe m: "))
    lista.append(m)

b=lista[0]
a=lista[0]
for j in range(n):
    if b<=lista[j]:
        b=lista[j]
    else:
        b=b

for k in range(n):
    if a>=lista[k]:
        a=lista[k]
    else:
        a=a

print("Najwiekszy element to: ",b)
print("Najmniejszy element to: ",a)