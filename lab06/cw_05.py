tablica=[]
x=[]
y=0
z=0
w=0
a=0
b=0
c = int(input("Jesli chcesz zakonczyc robienie tabeli wpisz 0"'\n'"Podaj liczbe ktora mam dodac do listy: "))
while c!=0:
    while c!=0:
        tablica.append(c)
        c = int(input("Podaj liczbe ktora mam dodac do listy: "))
    x+=[tablica]
    tablica = []
    c = int(input("Jesli chcesz zakonczyc robienie tabeli wpisz 0"'\n'"Podaj liczbe ktora mam dodac do listy: "))
    y+=1

for h in range(y):
    z=len(x[h])
    for g in range(z):
        w+=x[h][g]
        if h+1<y:
            b = len(x[(h + 1)])
            for n in range(b):
                a+=x[(h+1)][n]
    if h + 1 < y:
        if a>w:
            w=0
            b=h+1
        else:
            a=0
            b=h

print(x[b])