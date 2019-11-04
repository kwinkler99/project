n=str(input("Podaj napis: "))
tablica=[n]
c=''
d=''
while n:
    n = str(input("Podaj napis: "))
    if n:
        tablica.append(n)
b = len(tablica[0])
for i in range(len(tablica)):
    if len(tablica[i])>b:
        c=''
        c+=tablica[i]
        c+=', '
        b = len(tablica[i])
    elif len(tablica[i])==b:
        c+=tablica[i]
        c+=', '
b = len(tablica[0])
for j in range(len(tablica)):
    if len(tablica[j])<b:
        d=''
        d+=tablica[j]
        d+=', '
        b = len(tablica[j])
    elif len(tablica[j])==b:
        d+=tablica[j]
        d+=', '

print("Najdluzsze słowa to: ", c)
print("Najkrotsze słowa to: ", d)