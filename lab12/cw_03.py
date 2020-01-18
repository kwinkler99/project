f = open("liczby.txt", "r")
x = f.read().split("\n")

def sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if int(data[j]) > int(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]


sort(x)
print("Najwieksza to: ", x[len(x)-1])
print("Najmniejsza to: ", x[0])
f.close()