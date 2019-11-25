def funkcja(stała, zmienna):
    p = stała*zmienna
    print(zmienna,'*', stała,'=', p)

a=int(input("Podaj a: "))
n=int(input("Podaj n: "))
for i in range(1, n+1):
    funkcja(a,i)