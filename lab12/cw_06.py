imie = str(input("Podaj swoje imie: "))
nazwisko = str(input("Podaj swoje nazwisko: "))
w = 0
dane = imie + ' ' + nazwisko
plik = open('baza.txt', 'r')
x = plik.read().split('\n')
for i in range(len(x)):
    if x[i] == dane:
        print("Istniejesz juz w bazie danych")
        w = 1
if w == 0:
    print("Jeszcze cie nie ma w bazie danych")
