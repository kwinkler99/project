def suma(lista):
    if len(lista)==1: return lista[0]
    else: return suma(lista[1:])+lista[0]

lista=[10,11,20,21,30,31,90]
print(suma(lista))