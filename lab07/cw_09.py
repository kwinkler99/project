def NWW(a,b):
    dzielnik=NWD(a,b)
    print(dzielnik)
    return (a*b)/dzielnik

def NWD(a,b):
    if a>b:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                return i
    if b>a:
        for i in range(a,0,-1):
            if b%i==0 and a%i == 0:
                return i


liczba1=int(input("Podaj liczbe 1: "))
liczba2=int(input("Podaj liczbe 2: "))
print(NWW(liczba1,liczba2))