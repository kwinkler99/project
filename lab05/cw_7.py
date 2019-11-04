n=int(input("Podaj n: "))
m=int(input("Podaj m: "))

listan=[]
listam=[]
c=''

for i in range(n):
    x = str(input("Podaj do tablicy 1: "))
    listan.append(x)

for j in range(m):
    y = str(input("Podaj do tablicy 2: "))
    listam.append(y)

for i in range(n):
    for j in range(m):
        if listan[i]==listam[j]:
            c+=listan[i]
            c+=', '


print("Lista pierwsza to: ", listan)
print("Lista druga to: ", listam)
print("CZESCIA WSPOLNA TABLIC JEST: ", c)