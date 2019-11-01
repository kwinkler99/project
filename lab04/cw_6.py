n=str(input("Podaj pierwsze słowo: "))
m=str(input("Podaj drugie słowo: "))
x=0
c=str('')

for i in n:
    if i ==' ':
        x+=1
if x>=2:
    print("Wprowadziles wiecej slow niz 2")
else:
    if len(n)<len(m):
        for j in range(0, len(n),1):
            c+=n[j]
            c+=m[j]
        for k in range(len(n), len(m), 1):
            c+=m[k]
    else:
        for j in range(0, len(m),1):
            c+=n[j]
            c+=m[j]
        for k in range(len(m), len(n), 1):
            c+=n[k]


print(c)
