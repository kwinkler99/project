n=str(input("Podaj zdanie: "))
c=str('')

for i in n:
    if i =='ł':
        i = 'l'
    if i == 'ą':
         i='a'
    if i == 'ę':
        i ='e'
    if i == 'ó':
        i ='o'
    if i == 'ż':
        i ='z'
    if i == 'ś':
        i = 's'
    if i == 'ć':
        i = 'c'
    c+=i

print(c)
