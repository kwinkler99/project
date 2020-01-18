from string import ascii_lowercase
from string import ascii_uppercase
#**********************************

file = open('wiersz.txt').read()
ascii =[]
ascii2 =[]
l=[]
znaki=[" ","\n","\t"]
cyfry = []
for i in range(1000):
    cyfry.append(str(i))
for x in ascii_lowercase:
    ascii.append(x)
for x in ascii_uppercase:
    ascii2.append(x)
for x in file:
    l.append(x)
print("w wyrazie znajduja sie ", len([c for c in l if c  in ascii]) , "malych lietr")
print("w wyrazie znajduja sie ", len([c for c in l if c  in ascii2]), "dyzych liter")
print("w tekscie znajduje sie ", len([c for c in l if c  in cyfry]), "cyfr")
print("w tekscie znajduje sie ", len([c for c in l if c  in znaki]), "bialych znakow")

file.close()