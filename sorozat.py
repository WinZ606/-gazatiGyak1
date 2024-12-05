import random

def sorozatlista():
    i = 0
    lista = []
    while i < 8:
        szam1 = int(random.randint(-100,859))
        lista.append(szam1)
        i += 1
    return lista

def konzol_ir(lista):
    o = 0
    txt = ""
    while o < 8:
        if o == 7:
            txt += str(lista[o])
        else:
            txt += str(lista[o]) + ";"
        o += 1
    return txt
    
def tizzel_oszthatok_szama(lista):
    i = 0
    tizzelosztas = 0
    while (i < len(lista)):
        if (lista[i] % 10 == 0):
            tizzelosztas += 1
        i += 1
    return tizzelosztas

def fajlba_ir(txt):
    f = open("vegeredmeny.txt", "a")
    f.write(txt)
    f.close()