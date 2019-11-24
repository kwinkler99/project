matrix=[]
result=[]
lenght=0
tablica=[]
dl=0
wpis = int(input("Podaj liczbe ktora mam dodac do listy: "))
while wpis!=0:
    while wpis!=0:
        tablica.append(wpis)
        wpis = int(input("Podaj liczbe ktora mam dodac do listy: "))
    matrix+=[tablica]
    tablica = []
    wpis = int(input("Jesli chcesz zakonczyc robienie tabeli wcisnij enter"'\n'"Podaj liczbe ktora mam dodac do listy: "))
    lenght+=1

for k in range(lenght):
    print(matrix[k])
print('\n')

max=0
for i in matrix:
    max = len(i) if len(i) > max else max


for j in range(max):
    result.append([])
    for line in matrix:
        line = line + [0] * (max - len(line))
        if len(line) > j:
            result[j].append(line[j])


for end in range(max):
    print(str(result[end]).replace('0', ' '))



