def suma(liczba):
    if liczba==0: return 0
    else: return liczba%10 + suma(liczba//10)

print(suma(78192301))
