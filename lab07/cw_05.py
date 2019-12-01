import random
def funkcja (argument_n, z1,z2):
    tablica=[]
    if z1<z2:
        for i in range(argument_n):
            tablica.append(random.randint(z1,z2))
        return tablica
    if z2<z1:
        for i in range(argument_n):
            tablica.append(random.randint(z2,z1))
        return tablica







liczba_1 = int(input("Podaj ilosc w tablicy: "))
liczba_2 = int(input("Zakres pierwszy: "))
liczba_3 = int(input("Zakres drugi: "))
losowe=funkcja(liczba_1,liczba_2,liczba_3)
print(losowe)