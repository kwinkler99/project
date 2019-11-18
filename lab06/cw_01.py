n = int(input("Podaj liczbe n: "))
m = int(input("Podaj liczbe m: "))
tablica=[]
x=[]
for i in range(n):
    for j in range(m):
        k=float(input("Podaj wartosc ktora mam dodac do listy: "))
        tablica.append(k)
    x += [tablica]
    tablica = []
for k in range(n):
    print(x[k][::-1])

