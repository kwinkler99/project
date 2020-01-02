import math
punkt1 = {'x' : 1 , 'y' : 1}
punkt2 = {'x' : -20 , 'y' : -20}
punkt3 = {'x' : 5 , 'y' : 7}
punkt4 = {'x' : -19 , 'y' : -18}

lista=[punkt1, punkt2, punkt3, punkt4]


def odleglosc(lista):
    min = math.sqrt((lista[1]['x'] - lista[0]['x']) ** 2 + (lista[1]['y'] - lista[0]['y']) ** 2)
    punkt1 = [lista[0]]
    punkt2 = [lista[1]]
    for i in range (len(lista)):
        for j in range(len(lista)):
            if i != j:
                if math.sqrt((lista[j]['x'] - lista[i]['x']) ** 2 + (lista[j]['y'] - lista[i]['y']) ** 2) < min:
                    punkt1 = lista[i]
                    punkt2 = lista[j]
    print(punkt1)
    print(punkt2)

odleglosc(lista)

