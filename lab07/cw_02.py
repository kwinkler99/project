def funkcja1():
    wybor=str(input("Czy chcesz zakończyćprogram? (t/n)"))
    funkcja2(wybor)

def funkcja2(a):
    if a == 't':
        print("Koniec")
    if a =='n':
        funkcja1()


funkcja1()    