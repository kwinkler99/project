n=str(input("Podaj zdanie: "))
x=0
if n:
    x=1

for i in n:
    if i ==' ':
        x+=1


print("Zdanie ma ", x,"słów")