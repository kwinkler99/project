n=int(input("Podaj dlugosc wysokosc choinki: "))
x=1
z=n-1
y=n-2
for i in range(0, n, 1):
    print(z*" ", x*"*")
    x+=2
    z-=1

print(y*" ", "|_|")