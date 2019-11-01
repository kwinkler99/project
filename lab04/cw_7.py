n = str(input("Podaj słowo: "))
x = len(n)-1
z = int(x/2)
w = 0
c=''
y=''
for i in n:
    if w <= z:
        c+=n[x]
        y+=i
        x-=1
    else:
        break;
    w+=1


if y == c:
    print("Slowo jest palindromem")
elif y != c:
    print("Slowo nie jest palindromem")