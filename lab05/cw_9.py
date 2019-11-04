n=int(input("Podaj liczbe n: "))
m=int(input("Podaj liczbe m: "))
tablica=[]
tablica1=[]
c=''
for i in range(n):
    k=str(input("Podaj wartosc ktora mam dodac do listy 1: "))
    tablica.append(k)

for i in range(m):
    d=str(input("Podaj wartosc ktora mam dodac do listy 2: "))
    tablica1.append(d)

tablica.sort()
tablica1.sort()
tablica_sort=tablica+tablica1

for i in range(len(tablica_sort) - 1, 0, -1):
    for j in range(i):
        if tablica_sort[j] > tablica_sort[j + 1]:
            tablica_sort[j], tablica_sort[j + 1] = tablica_sort[j + 1], tablica_sort[j]


print(tablica)
print(tablica1)
print(tablica_sort)
