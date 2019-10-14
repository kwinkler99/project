x=int(input("Podaj liczbe calkowita: "))

if x>0:
    x=x
elif x<=0:
    x=-x



if x>=100 and x<1000:
    print("Liczba jest trzycyfrowa")
elif x>=10 and x<100:
    print("Liczba jest dwucyfrowa")
elif x>=0 and x<10:
    print("Liczba jest jednocyfrowa")
else:
    print("Liczba jest z poza zakresu")
