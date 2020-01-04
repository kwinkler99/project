lista = []


def create(a, b, c, d, e):
    adres = {'miasto': '', 'ulica': '', 'numer': ''}
    dane = {'imie': '', 'nazwisko': '', 'adres': adres}
    dane['adres']['miasto'] = a
    dane['adres']['ulica'] = b
    dane['adres']['numer'] = c
    dane['imie'] = d
    dane['nazwisko'] = e
    lista.append(dane)


create('sopot', 'gwiezdna', 30, 'Tomasz', 'Walczewski')
create('sopot', 'malutka', 90, 'Monika', 'Walczewska')
print(lista)


def read(imie, nazwisko):
    for i in range(len(lista)):
        if lista[i]['imie'] == imie and lista[i]['nazwisko'] == nazwisko:
            print(lista[i]['adres'])


read('Tomasz', 'Walczewski')


def read1(miasto):
    for i in range(len(lista)):
        if lista[i]['adres']['miasto'] == miasto:
            print(lista[i]['imie'], lista[i]['nazwisko'] + " adres: " + lista[i]['adres']['ulica'],
                  lista[i]['adres']['numer'])


read1('sopot')


def update(imie,nazwisko,ulica):
    for i in range(len(lista)):
        if lista[i]['imie'] == imie and lista[i]['nazwisko'] == nazwisko:
            lista[i]['adres']['ulica'] = ulica
    print(lista)


update('Tomasz', 'Walczewski', 'wielka')


def delete(nazwisko):
    for i,n in enumerate(lista):
        if lista[i]['nazwisko'] == nazwisko:
            lista.pop(i)
    print(lista)


delete('Walczewski')

def search(miasto):
    for i in range(len(lista)):
        if lista[i]['adres']['miasto'] == miasto:
            print(lista[i]['imie'], lista[i]['nazwisko'])

search('sopot')