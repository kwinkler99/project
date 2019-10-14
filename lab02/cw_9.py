x=int(input("Podaj liczbe w systemie dwojkowym: "))

z = 10
a = 0
b = 0
while z<=x:
        y = x%z
        if z > y and y >= z/10:
            b += 2**a
        a+=1
        z=z*10


y = x%z
if z > y and y >= z/10:
    b+=2**a

print("Liczba ta to: ", b)