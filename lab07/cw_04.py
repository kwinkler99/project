def trojkat(a,b,c):
    if check(a,b,c) == False:
        return 'Liczba ujemna'
    else:
        if a>b and a>b:
            if a< b+c:
                return 'MOZNA'
            else:
                return 'NIE MOZNA'
        elif b>a and b>c:
            if b<a+c:
                return 'MOZNA'
            else:
                return 'NIE MOZNA'
        elif c>a and c>b:
            if c<a+b:
                return 'MOZNA'
            else:
                return 'NIE MOZNA'


def check(a,b,c):
    if a>0 and b>0 and c>0:
        return True
    else:
        return False



liczba_1 = int(input("Podaj liczbe 1: "))
liczba_2 = int(input("Podaj liczbe 2: "))
liczba_3 = int(input("Podaj liczbe 3: "))
potwierdzenie=trojkat(liczba_1,liczba_2,liczba_3)
print(potwierdzenie)
