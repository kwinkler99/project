n = int(input("Podaj liczbe n: "))
x=1

for i in range(n):
    x = x*n
    n -= 1


print("n!=", x)