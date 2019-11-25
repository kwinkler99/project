def check(napis):
    prawda = 0
    for i in napis:
        if set(napis) >= set('abcdefghijklmnoprstuvwqxy'):
            prawda=1
    if prawda == 1:
        return True
    else:
        return False



n=str(input("Podaj napis do sprawdzenia: "))
print(check(n))