x=int(input("Podaj liczbe: "))
y=int(input("Podaj liczbe: "))
if x>y:
    if x%y == 0:
        print("najwiekszy wspolny dzielnik to ", y)
    else:
        z=y
        while (x%z!=0 or y%z!=0):
            z-=1
        print("najwiekszy wspolny dzielnik to ", z)
elif y>x:
    if y%x == 0:
        print("najwiekszy wspolny dzielnik to ", x)
    else:
        z = x
        while (x%z!=0 or y%z!=0):
            z -= 1
        print("najwiekszy wspolny dzielnik to ", z)




