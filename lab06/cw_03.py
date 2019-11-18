n = int(input("Podaj liczbe n: "))
m = int(input("Podaj liczbe m: "))
tablica=[]
x=[]
y=[]
for i in range(n):
    for j in range(m):
        k=float(input("Podaj wartosc ktora mam dodac do pierwszej listy: "))
        tablica.append(k)
    x += [tablica]
    tablica = []

for h in range(n):
    for l in range(m):
        k=float(input("Podaj wartosc ktora mam dodac do drugiej listy: "))
        tablica.append(k)
    y += [tablica]
    tablica = []
for k in range(n):
    print(x[k])
print('\n')
for k in range(n):
    print(y[k])
print('\n')
for k in range(n):
    for w in range(m):
        x[k][w]=x[k][w]+y[k][w]
    print(x[k])

