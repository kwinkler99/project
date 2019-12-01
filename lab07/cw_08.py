def number(a):
    test=0
    if a>10:
        for i in range(2,11):
            if a%i == 0:
               test=1
        if test==1:
            return False
        else:
            return True
    else:
        if a == 5 or a == 2 or a == 3 or a == 7:
            return True
        else:
            return False




liczba=int(input("Podaj liczbe: "))
print(number(liczba))
