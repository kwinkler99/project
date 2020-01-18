import sys, os
while 1:
    try:
        f = open("pliczek.txt", "ab")
        plik = str(input("Podaj nazwe pliku ktory chcesz otworzyc: "))
        l = open(plik+'.txt', "r")
        x = int(input("Proszę wprowadzić liczbę: "))
        y = int(input("Prosze wprowadzic liczbe: "))
        z = x/y
        print("liczba pierwsza/liczbe druga = ", z)
        lista = [x,y,z]
        print(lista)
        w = int(input("Prosze wprowadzic ktora liste chcesz wyswietlic: "))
        print(lista[w])
        slownik = {'liczba1': x, 'liczba2': y, 'liczba3': z}
        nazw = str(input("Podaj ktora liczbe chcesz wybrac (liczba1/liczba2/liczba3:"))
        print(slownik[nazw])
        odp = str(input("Czy chcesz dodac cos do liczby(yes/no): "))
        if odp == 'yes':
            name = input("Wpisz swoje imie: ")
            number = int(input("Podaj liczbe ktora chcesz dodac: "))
            x.append(number)
        print("Twoje imie to: " + name)
        m = str(input("Podaj liczbe1: "))
        n = str(input("Podaj liczbe2: "))
        print(m/n)
    except ZeroDivisionError:
        print("Nie mozna dzielic przez 0")
    except IndexError:
        print("Index jest spoza zakresu")
    except ValueError:
        print("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")
    except KeyError:
        print("Takiego wyboru nie było!")
    except AttributeError:
        print("Nie można dodawać nic do liczb, jedynie liczby mozna dodac do listy!")
    except NameError:
        print("Przeciez nie podawales imienia :P sprobuj jeszcze raz")
    except FileExistsError:
        print("Ten plik juz istnieje")
    except FileNotFoundError:
        print("Ten plik chyba nie istnieje")
    except TypeError:
        print("liczba nie jest integer")
    else:
        print("Cos poszlo nie tak, sprobuj jeszcze raz")


