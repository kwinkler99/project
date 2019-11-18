k=int(input("Podaj liczbe k: "))
tablica=[]
x=[]
y=0
z=0

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
        x[h][g]=x[h][g]*k
    print(x[h])
