a=float(input("Podaj liczbe a: "))
b=float(input("Podaj liczbe b: "))
c=float(input("Podaj liczbe c: "))
delta=b*b-4*a*c
if delta>0:
    print("Rownanie ma dwa pierwiastki")
elif delta==0:
    print("Rownanie ma jeden pierwiastek")
else:
    print("Rownanie nie ma pierwiastkow")

