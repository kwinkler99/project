lista = []

def create(a,b,c,d,e):
    dane = {'marka': c, 'nr_rej': d, 'przejechane': e}
    samochod = {'imie': a, 'nazwisko': b, 'dane': dane}
    lista.append(samochod)


create('Karol','Kowalski', 'Ford', '1234', '100tys.')
create('Maciek','Janowicz', 'Opel', '34553', '500tys.')
create('Monika','Pawlicka', 'Skoda', '1234', '600tys')
create('Anna','Wisniewska','Opel','67866', '600tys')
print(lista)

def read(nr):
    for i in range(len(lista)):
        if lista[i]['dane']['nr_rej'] == nr:
            print('Dane wlasciciela: ' + lista[i]['imie'], lista[i]['nazwisko'])


read('1234')

def update(nr,imie,nazwisko):
    for i in range(len(lista)):
        if lista[i]['dane']['nr_rej'] == nr:
            lista[i]['imie'] = imie
            lista[i]['nazwisko'] = nazwisko
            print(lista[i])

update('67866','Asia','Mariacka')

def delete(nazwisko):
    for i,n in enumerate(lista):
        if lista[i]['nazwisko'] == nazwisko:
            lista.pop(i)
            print(lista)

delete('Kowalski')

create('Ada','Pawlicka', 'Ford', '1232344', '300tys')


def search(il):
    y = 1
    for i in range(len(lista)):
        nazw = lista[i]['nazwisko']
        for j in range(i+1, len(lista)):
            if nazw == lista[j]['nazwisko']:
                y+=1
        if y >= il:
            print(lista[i]['imie'], lista[i]['nazwisko'])
            y = 1


search(2)