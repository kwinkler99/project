x=[]
y=0
dl=0
tablica=[]
tablica1=[]
wpis = str(input("Podaj liczbe ktora mam dodac do listy: "))
while wpis:
    while wpis:
        tablica.append(wpis)
        wpis = str(input("Podaj liczbe ktora mam dodac do listy: "))
    x+=[tablica]
    tablica = []
    wpis = str(input("Jesli chcesz zakonczyc robienie tabeli wcisnij enter"'\n'"Podaj liczbe ktora mam dodac do listy: "))
    y+=1

for i in range (y):
    dl = len(x[i])
    for j in range (dl):
        tablica1.append(x[i][j])

print(x)
print(tablica1)
