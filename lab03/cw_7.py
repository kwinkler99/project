n=int(input("Podaj dlugosc swoich gwaizdeczek: "))
x=n+1
z=n


for i in range(0, n+1, 1):
    x -= 1
    print(x*" ", i*"*")
print("\r")
for i in range(n, 0, -1):
    print(x*" ", i*"*")
    x+=1


