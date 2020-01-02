lista = []

def create(id,imie,nazwisko,pesel,wiek):
    osoby = {'id': id, 'imie': imie, 'nazwisko': nazwisko, 'pesel': pesel, 'wiek': wiek}
    return osoby


lista.append(create(5,'kasia','winkler',900000000,30))
lista.append(create(10,'kasia','winkler',900000000,30))
lista.append(create(2,'kasia','winkler',900000000,30))
lista.append(create(3,'kasia','winkler',900000000,30))
print(lista)


def read(id):
    lista1=[]
    for i in range(len(lista)):
        if lista[i]['id'] == id:
            lista1.append(lista[i]['id'])
            lista1.append(lista[i]['imie'])
            lista1.append(lista[i]['nazwisko'])
            lista1.append(lista[i]['pesel'])
            lista1.append(lista[i]['wiek'])
    return lista1


krotka =(read(3))
print(krotka)


def update(id,imie,nazwisko,pesel,wiek):
    for i in range(len(lista)):
        if lista[i]['id'] == id:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
            lista[i]['pesel'] = pesel
            lista[i]['wiek'] = wiek
        if lista[i]['imie'] == imie:
            lista[i]['id'] = id
            lista[i]['nazwisko'] = nazwisko
            lista[i]['pesel'] = pesel
            lista[i]['wiek'] = wiek
        if lista[i]['nazwisko'] == nazwisko:
            lista[i]['imie'] = imie
            lista[i]['id'] = id
            lista[i]['pesel'] = pesel
            lista[i]['wiek'] = wiek
        if lista[i]['pesel'] == pesel:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
            lista[i]['id'] = id
            lista[i]['wiek'] = wiek
        if lista[i]['wiek'] == wiek:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
            lista[i]['pesel'] = pesel
            lista[i]['id'] = id


update(3,'Ala','KOWALSKA',909090902,21)
print(lista)


def delete(id):
    for i in range(len(lista)):
        if lista[i]['id'] == id:
            lista.remove(lista[i])
            break


delete(5)
print(lista)


