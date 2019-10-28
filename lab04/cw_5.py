n=str(input("Podaj 6 znakow: "))
x=0
for i in n:
    if i ==' ':
        x+=1

if x>6:
    print("za dlugie slowo")
else:
    print (n[4])
    print (n[1:4])

if x>6:
    print("za dlugie slowo")
else:
    print (n[-2])
    print (n[-5:-2])