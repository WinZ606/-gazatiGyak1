from Huzas import Huzas

def beolvas():
    huzas_lista = []
    f = open("huzasok.txt", "r", encoding="UTF-8")
    elso_sor = f.readline()
    sorok = f.readlines()
    for i in range(0,len(sorok),1):
        sor = sorok[i].strip()
        sor_lista = sor.split("@")
        huzas = Huzas(int(sor_lista[0]),int(sor_lista[1]),int(sor_lista[2]),int(sor_lista[3]))
        huzas_lista.append(huzas)
    f.close()
    return huzas_lista

def beolvasasok(huzas_lista):
    for i in range(0,len(huzas_lista),1):
        print(huzas_lista[i])

#beolvasasok(beolvas())

def feladat1(huzasok):
    print(f"III/A, B:\nHúzások száma: {huzasok[-1].huzas}")

def feladat2(huzasok):
    i = 0
    osszeg:float = 0
    mennyiseg:float = 0
    while (i < len(huzasok)):
        if (huzasok[i].het == 42):
            osszeg += (huzasok[i].szam)
            mennyiseg += 1
        i += 1
    atlag = float(osszeg / mennyiseg)
    print(f"III/C:\nA 43. héten húzott számok átlaga: {atlag}")

def feladat3(huzasok):
    i = 0
    indexe = 0
    while (i < len(huzasok)):
        if (huzasok[i].szam > huzasok[indexe].szam ):
            indexe = i
        i += 1
    print(f"III/D:\nAz első legnagyobb kihúzott szám értéke: {huzasok[indexe].szam}, {huzasok[indexe].ev}, a {huzasok[indexe].het}. héten húzták ki, ez volt a {huzasok[indexe].huzas}. húzás.")