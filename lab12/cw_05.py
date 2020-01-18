import random
lista = []
y = 0
lotto = open('lotto.txt', 'w')
for i in range(6):
    x = random.randint(1,49)
    for j in range(len(lista)):
        if lista[j] == x:
            y = 1
    if y == 0:
        lotto.write(str(x)+', ')
        y = 0
    lista.append(x)

lotto.close()
