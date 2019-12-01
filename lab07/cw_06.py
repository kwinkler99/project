def check(napis):
    prawda = 0
    for i in napis:
        if set(napis) >= set('abcdefghijklmnoprstuvwqxy'):
            if i != 'ą' and i != 'ę' and i != 'ć' and i != 'ż' and i != 'ń' and i != 'ś' and i != 'ó' and i != 'ł':
                prawda=1
            else:
                prawda=0
                break
    if prawda == 1:
        return True
    else:
        return False



n=str(input("Podaj napis do sprawdzenia: "))
print(check(n))