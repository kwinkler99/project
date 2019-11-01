napis1 = str(input("Podaj pierwsza liczbe w systemie szesnastkowym : 0x"))
napis2 = str(input("Podaj pierwsza liczbe w systemie szesnastkowym : 0x"))
x = 0
y = 0
z = 0
r = 0
k = 1
c = ''
v = len(napis1)
w = len(napis2)
for i in range(1, v+1, 1):
    if napis1[-i] == '0':
        x = 0
    if napis1[-i] == '1':
        x = 1
    if napis1[-i] == '2':
        x = 2
    if napis1[-i] == '3':
        x = 3
    if napis1[-i] == '4':
        x = 4
    if napis1[-i] == '5':
        x = 5
    if napis1[-i] == '6':
        x = 6
    if napis1[-i] == '7':
        x = 7
    if napis1[-i] == '8':
        x = 8
    if napis1[-i] == '9':
        x = 9
    if napis1[-i] == 'A':
        x = 10
    if napis1[-i] == 'B':
        x = 11
    if napis1[-i] == 'C':
        x = 12
    if napis1[-i] == 'D':
        x = 13
    if napis1[-i] == 'E':
        x = 14
    if napis1[-i] == 'F':
        x = 15
    if k <= w:
        if napis2[-k] == '0':
            y = 0
        if napis2[-k] == '1':
            y = 1
        if napis2[-k] == '2':
            y = 2
        if napis2[-k] == '3':
            y = 3
        if napis2[-k] == '4':
            y = 4
        if napis2[-k] == '5':
            y = 5
        if napis2[-k] == '6':
            y = 6
        if napis2[-k] == '7':
            y = 7
        if napis2[-k] == '8':
            y = 8
        if napis2[-k] == '9':
            y = 9
        if napis2[-k] == 'A':
            y = 10
        if napis2[-k] == 'B':
            y = 11
        if napis2[-k] == 'C':
            y = 12
        if napis2[-k] == 'D':
            y = 13
        if napis2[-k] == 'E':
            y = 14
        if napis2[-k] == 'F':
            y = 15
    else:
        y = 0
    k+=1
    z = (x+y)%16+r
    r = int((x+y)/16)
    if z == 0:
        c += '0'
    if z == 1:
        c += '1'
    if z == 2:
        c += '2'
    if z == 3:
        c += '3'
    if z == 4:
        c += '4'
    if z == 5:
        c += '5'
    if z == 6:
        c += '6'
    if z == 7:
        c += '7'
    if z == 8:
        c += '8'
    if z == 9:
        c += '9'
    if z == 10:
        c += 'A'
    if z == 11:
        c += 'B'
    if z == 12:
        c += 'C'
    if z == 13:
        c += 'D'
    if z == 14:
        c += 'E'
    if z == 15:
        c += 'F'

txt = c[::-1]
print(txt)