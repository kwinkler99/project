tablica=[]
result=[['0','1','2','3','4','5','6','7','8']]
a=0
b=0
c=0
d=0

for j in range (9):
    for i in range(8):
        if i == 0:
            tablica.append([j+1])
        tablica.append(' ')
    result+=[tablica]
    tablica=[]


for j in range(9):
    print(result[j])



wiersz1 = int(input("PODAJ WSPOLRZEDNE HETMANA 1 (wiersz): ")) - 1
kol1 = int(input("PODAJ WSPOLRZEDNE HETMANA 1 (kolumna): ")) - 1
wiersz2 = int(input("\nPODAJ WSPOLRZEDNE HETMANA 2 (wiersz): ")) - 1
kol2 = int(input("PODAJ WSPOLRZEDNE HETMANA 2 (kolumna): ")) - 1
wiersz3 = int(input("\nPODAJ WSPOLRZEDNE HETMANA 3 (wiersz): ")) - 1
kol3 = int(input("PODAJ WSPOLRZEDNE HETMANA 3 (kolumna): ")) - 1
result=[['0','1','2','3','4','5','6','7','8']]
for i in range (9):
    for j in range(8):
        if j == 0:
            tablica.append([i+1])
        if (i==wiersz1 and j==kol1) or (i == wiersz2 and j == kol2) or (i == wiersz3 and j == kol3):
            tablica.append('H')
        else:
            tablica.append(' ')
    result+=[tablica]
    tablica=[]

for j in range(9):
    print(result[j])

pionek_w = int(input("\nPODAJ WSPOLRZEDNE PIONKA (wiersz): ")) - 1
pionek_k = int(input("PODAJ WSPOLRZEDNE PIONKA (kolumna): ")) - 1
result=[['0','1','2','3','4','5','6','7','8']]
for i in range (9):
    for j in range(8):
        if j == 0:
            tablica.append([i + 1])
        if (i==wiersz1 and j==kol1) or (i == wiersz2 and j == kol2) or (i == wiersz3 and j == kol3):
            tablica.append('H')
        elif i == pionek_w and j==pionek_k:
            tablica.append('P')
        else:
            tablica.append(' ')
    result+=[tablica]
    tablica=[]
for j in range(9):
    print(result[j])
if pionek_w == wiersz1 or pionek_w == wiersz2 or pionek_w == wiersz3:
    print("Pionek zbity")
elif pionek_k == kol1 or pionek_k == kol2 or pionek_k == kol3:
    print("Pionek zbity")



if pionek_w < wiersz1 and pionek_k > kol1:
    max = wiersz1 if wiersz1 < 8-kol1 else 8-kol1
    a=1
elif pionek_w < wiersz1 and pionek_k < kol1:
    max = wiersz1 if wiersz1 < kol1 else kol1
    b=1
elif pionek_w > wiersz1 and pionek_k < kol1:
    max = 8 - wiersz1 if 8-wiersz1 < kol1 else kol1
    c=1
elif pionek_w > wiersz1 and pionek_k > kol1:
    max = 8 - wiersz1 if 8 - wiersz1 < 8 - kol1 else 8 - kol1
    d=1

for pole in range (max):
    if a==1:
        if result[wiersz1 + 1 - pole][kol1 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz1 + 1 - pole >= 0 and kol1 + 1 + pole >= 0:
            print("Pionek zbity")
    if b==1:
        if result[wiersz1 + 1 - pole][kol1 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz1 + 1 - pole >= 0 and kol1 + 1 - pole >= 0:
            print("Pionek zbity")
    if c==1:
        if result[wiersz1 + 1 + pole][kol1 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz1 + 1 + pole >= 0 and kol1 + 1 - pole >= 0:
            print("Pionek zbity")
    if d==1:
        if result[wiersz1 + 1 + pole][kol1 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz1 + 1 + pole >= 0 and kol1 + 1 + pole >= 0:
            print("Pionek zbity")
a=0
b=0
c=0
d=0


if pionek_w < wiersz2 and pionek_k > kol2:
    max = wiersz2 if wiersz2 < 8-kol2 else 8-kol2
    a=1
elif pionek_w < wiersz2 and pionek_k < kol2:
    max = wiersz2 if wiersz2 < kol2 else kol2
    b=1
elif pionek_w > wiersz2 and pionek_k < kol2:
    max = 8 - wiersz2 if 8-wiersz2 < kol2 else kol2
    c=1
elif pionek_w > wiersz2 and pionek_k > kol2:
    max = 8 - wiersz2 if 8 - wiersz2 < 8 - kol2 else 8 - kol2
    d=1

for pole in range(max):
    if a==1:
        if result[wiersz2 + 1 - pole][kol2 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz2 + 1 - pole >= 0 and kol2 + 1 + pole >= 0:
            print("Pionek zbity")
    if b==1:
        if result[wiersz2 + 1 - pole][kol2 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz2 + 1 - pole >= 0 and kol2 + 1 - pole >= 0:
            print("Pionek zbity")
    if c==1:
        if result[wiersz2 + 1 + pole][kol2 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz2 + 1 + pole >= 0 and kol2 + 1 - pole >= 0:
            print("Pionek zbity")
    if d==1:
        if result[wiersz2 + 1 + pole][kol2 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz2 + 1 + pole >= 0 and kol2 + 1 + pole >= 0:
            print("Pionek zbity")
a=0
b=0
c=0
d=0


if pionek_w < wiersz3 and pionek_k > kol3:
    max = wiersz3 if wiersz3 < 8-kol3 else 8-kol3
    a=1
elif pionek_w < wiersz3 and pionek_k < kol3:
    max = wiersz3 if wiersz3 < kol3 else kol3
    b=1
elif pionek_w > wiersz3 and pionek_k < kol3:
    max = 8 - wiersz3 if 8-wiersz3 < kol3 else kol3
    c=1
elif pionek_w > wiersz3 and pionek_k > kol3:
    max = 8 - wiersz3 if 8 - wiersz3 < 8 - kol3 else 8 - kol3
    d=1

for pole in range(max):
    if a==1:
        if result[wiersz3 + 1 - pole][kol3 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz3 + 1 - pole >= 0 and kol3 + 1 + pole >= 0:
            print("Pionek zbity")
    if b==1:
        if result[wiersz3 + 1 - pole][kol3 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz3 + 1 - pole >= 0 and kol3 + 1 - pole >= 0:
            print("Pionek zbity")
    if c==1:
        if result[wiersz3 + 1 + pole][kol3 + 1 - pole] == result[pionek_w + 1][pionek_k + 1] and wiersz3 + 1 + pole >= 0 and kol3 + 1 - pole >= 0:
            print("Pionek zbity")
    if d==1:
        if result[wiersz3 + 1 + pole][kol3 + 1 + pole] == result[pionek_w + 1][pionek_k + 1] and wiersz3 + 1 + pole >= 0 and kol3 + 1 + pole >= 0:
            print("Pionek zbity")
a=0
b=0
c=0
d=0