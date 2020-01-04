lista = []


def create(a, b, c, d, e):
    przedmioty = {'matematyka': '', 'polski': '', 'angielski': ''}
    dane = {'imie': a, 'nazwisko': b, 'oceny': przedmioty}
    dane['oceny']['matematyka'] = c
    dane['oceny']['polski'] = d
    dane['oceny']['angielski'] = e
    lista.append(dane)
    print(lista)


create('kasia', 'kowalska', 5, 4, 6)
create('mateusz', 'walczewski', 3, 3, 2)
create('ola', 'zielinska', 5, 4, 4)
create('lukasz', 'lubnicki', 4, 5, 6)
create('maciek', 'kowalski', 2, 2, 3)
create('olek', 'wielki', 6, 6, 6)


def read(nazwisko):
    for i in range(len(lista)):
        if lista[i]['nazwisko'] == nazwisko:
            print(lista[i]['oceny'])


read('walczewski')

def update(nazwisko,przedmiot, ocena):
    for i in range(len(lista)):
        if lista[i]['nazwisko'] == nazwisko:
            lista[i]['oceny'][przedmiot] = ocena
    print(lista)


update('walczewski', 'polski', 6)


def delete(nazwisko):
    for i,n in enumerate(lista):
        if lista[i]['nazwisko'] == nazwisko:
            lista.pop(i)
    print(lista)


delete('walczewski')


def search(srednia):
    for i in range(len(lista)):
        if (lista[i]['oceny']['matematyka']+lista[i]['oceny']['polski']+lista[i]['oceny']['angielski'])/3 >= srednia:
            print(lista[i]['imie'], lista[i]['nazwisko'])

search(3)
search(5)

