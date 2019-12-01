def max_number(tablica, n):
    number1=0
    pozycja=0
    tablica1=[]
    for j in range (n):
        for i in tablica:
            if i>number1:
                number1 = i
        tablica1.append(number1)
        for k in tablica:
            if k == number1:
                tablica.pop(pozycja)
            pozycja += 1
        number1=0
        pozycja=0
    return tablica1[len(tablica1)-1]




tablica=[]
for i in range(10):
    n=int(input("Podaj liczbe do listy: " ))
    tablica.append(n)
m=int(input("Podaj n-ty element co do wielkości: "))
print(max_number(tablica, m))