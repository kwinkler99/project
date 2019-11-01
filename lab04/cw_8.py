n = str(input("Podaj słowo: "))
m = str(input("Podaj podsłowo: "))

v = 0
y=0
c=''
z = 0
for j in range(len(n)-1):
    for i in n:
        if v < len(m):
            c += i
            v += 1
        else:
            if c == m:
                y = 1
                break
            else:
                c = ''
                v = 0
                n = n[1:]
                break

if y == 1:
    print("Podsłowo zawiera sie w słowie")
else:
    print("Podsłowo nie zawiera sie w słowie")
