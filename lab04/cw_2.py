n=str(input("Podaj slowo: "))
x=0

for i in n:
    if i =='a':
        x+=1
    if i == 'e':
         x += 1
    if i == 'i':
         x += 1
    if i == 'o':
         x += 1
    if i == 'u':
         x += 1
    if i == 'y':
         x += 1

print("Samoglosek jest: ", x)