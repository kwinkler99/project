t=float(input("Podaj tempreature: "))
if(t>-50 and t<50):
    if t<0:
        if t>=-15:
            print("zimno")
        else:
            print("bardzo zimno")

    elif t>=0:
        if t<=15:
            print("cieplo")
        else:
            print("bardoz cieplo")
else:
    print("temperatura poza skala")