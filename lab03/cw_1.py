x = int(input("Podaj liczbe x: "))
z=0
liczba=0

for i in range(x):
    liczba += z
    z=int(input("Podaj liczbe z: "))

print("Srednia liczb to ", z/x)