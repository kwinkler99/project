def first(a,b,c):
    if a>b and a>b:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c

def second(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c


liczba_1=int(input("Podaj liczbe 1: "))
liczba_2=int(input("Podaj liczbe 2: "))
liczba_3=int(input("Podaj liczbe 3: "))

najwieksza=first(liczba_1,liczba_2,liczba_3)
najmniejsza=second(liczba_1,liczba_2,liczba_3)
print("Najwieksza to: ",najwieksza)
print("Najmnijsza to: ",najmniejsza)