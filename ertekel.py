def feladat1():
    print("I/A, B: ")
    hetnapja = str(input("Hét napja: "))
    oraneve = str(input("Óra neve: "))
    ertekeles = int(input("Értékelés (0-5): "))
    print(" ")
    while (ertekeles >= 6) or (ertekeles < 0):
        if (ertekeles <= -1):
          ertekeles = int(input("Az értékelés nem lehet negatív "))
        elif (ertekeles >= 6):
            ertekeles = int(input("5 pont feletti értékelés nem elfogadható "))
            
    print("I/C: ")
    print("Köszönjük az értékelést!")
    print(f"Összefoglaló: {hetnapja}, {oraneve}, {ertekeles} érték")
