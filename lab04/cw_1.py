n = str(input("podaj słowo numer 1: "))
n1 = str(input("podaj słowo numer 2: "))

if n < n1:
    print("Leksykalnie: ", n)
else:
    print("Leksykalnie: ", n1)

if len(n) > len(n1):
    print("Dluzszym slowem jest: ", n)
else:
    print("Dluzszym slowem jest: ", n1)

