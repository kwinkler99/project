słownik ={ 1 : "niedostateczny", 2 : "dopuszczajacy" , 3 : "dostateczny", 4 : "dobry", 5 : "bardzo dobry", 6 : "celujacy"}

print(słownik[1])

del słownik[1], słownik[6]

słownik['3+'] = "dostateczna plus"
słownik['2+'] = "dopuszczajacy plus"
słownik['4+'] = "dobry plus"

print(słownik)