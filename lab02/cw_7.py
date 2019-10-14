x=float(input("Podaj liczbe: "))
d = 0
u = 0
while x!=0:
    if x>=0:
        d+=1
    elif x<0:
        u+=1
    x=0
    x = float(input("Podaj ponownie liczbe: "))


print("Dodatnich liczb było: ", d)
print("Ujemnych liczb bylo: ", u)