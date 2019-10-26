n=int(input("Podaj liczbe n: "))
x=1
y=1
z=1
w=1
p=1
for i in range(0, n):
    if (x == n+1):
        x = 1
    for i in range(0,n):
        if (y == n+1):
            y = 1
        for i in range(0,n):
            if (z == n+1):
                z = 1
            for i in range(0,n):
                if (p == n+1):
                    p = 1
                for i in range(0 ,n):
                    print(x, y, z, p, w)
                    w += 1
                    if (w == n+1):
                        w = 1
                p += 1
            z += 1
        y += 1
    x += 1
