lista = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

parzyste = open('parzyste.txt', 'w')
nieparzyste = open('nieparzyste.txt', 'w')

for i in range(len(lista)):
    if int(lista[i])%2 == 0:
        parzyste.write(lista[i]+ ', ')
    else:
        nieparzyste.write(lista[i]+ ', ')

parzyste.close()
nieparzyste.close()