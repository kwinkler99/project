def czyszczenie(tablica):
    x=0
    y=0
    for i in tablica:
        for j in tablica:
            if y+1<len(tablica):
                if tablica[x] == tablica[y+1] and x != y+1:
                    tablica.pop(y+1)
                y+=1
        x+=1
        y=0








tablica=[]
for i in range(10):
    n=int(input("Podaj liczbe do listy: " ))
    tablica.append(n)
czyszczenie(tablica)
print(tablica)