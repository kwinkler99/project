lista = []

def create(a, b, c):
    dane = {'stolica': b, 'ludnosc': c}
    kraj = {'panstwo': a, 'dane': dane}
    lista.append(kraj)

create('Polska', 'Warszawa', 37.98)
create('Czechy', 'Praga', 10.65)
create('Niemcy', 'Berlin', 82.79)


print(lista)

def read(stolica):
    for i in range(len(lista)):
        if lista[i]['dane']['stolica'] == stolica:
            print('panstwo: ' + lista[i]['panstwo'] + ', ludnosc: ' + str(lista[i]['dane']['ludnosc']) + ' miliona')

read('Praga')


def update(pan, a, b):
    for i in range (len(lista)):
        if lista[i]['panstwo'] == pan:
            lista[i]['dane']['stolica'] = a
            lista[i]['dane']['ludnosc'] = b
            print(lista[i])


update('Polska', 'Gdansk', '40')


def delete(stolica):
    for i, n in enumerate(lista):
        if lista[i]['dane']['stolica'] == stolica:
            lista.pop(i)
            print(lista)

delete('Praga')


def search(a):
    for i in range(len(lista)):
        if int(lista[i]['dane']['ludnosc']) > a:
            print(lista[i])

search(15)