m=[]
tablica=[]
for i in range (1,11):
    for j in range (1,11):
        tablica.append(j*i)
    m+=[tablica]
    tablica=[]

for k in range(10):
    print(m[k])
