tablica=[]
x=[]
y=0
dl1=0
tab1=0
tab2=0
dl2=0
m=0
m1=0
mx=0
m1x=0
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
    dl1=len(x[h])
    for g in range(dl1):
        tab1+=x[h][g]
    if h+1<y:
        dl2 = len(x[(h + 1)])
        for n in range(dl2):
            tab2+=x[(h+1)][n]
    if h + 1 < y:
        if h==0 and tab1>tab2:
            m=h
            mx=tab1
        if tab2>tab1:
            m1x=tab2
            tab2=0
            tab1=0
            m1=h+1
        else:
            tab2=0
            tab1=0
if mx>m1x:
    print(x[m])
else:
    print(x[m1])