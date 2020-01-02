data1 = {'dzien' : 1 ,'miesiac' : 3 ,'rok' : 1999}
data2 = {'dzien' : 30 ,'miesiac' : 3 ,'rok': 1999}
data3 = {'dzien' : 3 ,'miesiac': 12 ,'rok' : 2012}
data4 = {'dzien' : 10 ,'miesiac': 6 ,'rok' : 2019}
lista = [data1,data2,data3,data4]


def sort(n):
    for i in range(len(n)):
        if i + 1 < len(n):
            if n[i]['rok'] > n[i+1]['rok']:
                n[i], n[i + 1] = n[i + 1], n[i]
            if n[i]['rok'] == n[i+1]['rok']:
                if n[i]['miesiac'] > n[i + 1]['miesiac']:
                    n[i], n[i + 1] = n[i + 1], n[i]
                if n[i]['miesiac'] == n[i + 1]['miesiac']:
                    if n[i]['dzien'] > n[i + 1]['dzien']:
                        n[i], n[i + 1] = n[i + 1], n[i]


sort(lista)
for i in range (len(lista)):
    print(lista[i])