n = int(input("Podaj liczbe n: "))
tablica=[]
x=[]
liczba=0
for i in range (n):
    for j in range (n):
        c=int(input("Podaj liczbe do tablicy: "))
        tablica.append(c)
    x+=[tablica]
    tablica=[]
for k in range (n):
    print(x[k])

for m in range (n):
    for l in range(n):
        if m == l:
            liczba += x[m][l]
for m in range (n-1,-1,-1):
    for l in range (n-1,-1,-1):
        if m == l:
            liczba += x[m][l]
d=int(n/2)
liczba -= x[d][d]
print(liczba)
