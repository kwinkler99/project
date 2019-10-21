h=str(input("Podaj hasło: "))
i=int(input("Ile razy powtorzyc? "))

for a in range(i):
    x = str(input("Podaj hasło: "))
    while x != h:
        x = str(input("Podaj hasło: "))

print("Dziekuje podales prawidlowe haslo", i, "razy" )