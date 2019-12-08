def czyszczenie(tablica):
    x=0
    y=1
    for i in tablica:
        for j in tablica:
            if y<len(tablica):
                if i == j and x != y:
                    tablica.pop(y)
                    y-=1
                y+=1
        x+=1
        y=1
    if tablica[0] == tablica[len(tablica) - 1]:
        tablica.pop(len(tablica) - 1)








tablica=[]
for i in range(10):
    n=int(input("Podaj liczbe do listy: " ))
    tablica.append(n)
czyszczenie(tablica)
print(tablica)