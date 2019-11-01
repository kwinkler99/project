n = str(input("Podaj słowo: "))
x = len(n)-1
z = int(x/2)
y = 0
for i in n:
    if i != n[z]:
        if i == n[x]:
            y=1
            x-=1
        else:
            x-=1
            y=0
    else:
        break;


if y == 1:
    print("Slowo jest palindromem")