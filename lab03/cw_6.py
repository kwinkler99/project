n=int(input("Podaj dlugosc swoich gwaizdeczek: "))

for i in range(0, n+1, 1):
         print(i*"*")
print("\r")
for i in range(n, 0, -1):
         print(i*"*")


