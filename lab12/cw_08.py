file = open('znaki.txt', 'r')
x = file.read().split('\n')
slowo = ''
lista= []
ilosc = 0
for i in range (len(x)):
    for j in range(int(len(x[i])-1), -1, -1):
        slowo += x[i][j]
    lista.append(slowo)
    slowo = ''
    if x[i] == lista[i]:
        ilosc += 1
        palidrom = open('palindrom.txt', 'a')
        palidrom.write(x[i] + '\n')
palidrom.close()
file.close()
print("palindromow jest: ", ilosc)