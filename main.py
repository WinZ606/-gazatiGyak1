import ertekel
import sorozat
import hatoslotto
from Huzas import Huzas

ertekel.feladat1()
lista = sorozat.sorozatlista()
print(f"II/A, B, C: \n{sorozat.konzol_ir(lista)}")
tizzeloszthatok = sorozat.tizzel_oszthatok_szama(lista)
print(f"II/D, E: \nTízzel osztható számok száma: {tizzeloszthatok}.")
sorozat.fajlba_ir(sorozat.konzol_ir(lista))
beolvas = hatoslotto.beolvas()
hatoslotto.feladat1(beolvas)
hatoslotto.feladat2(beolvas)
hatoslotto.feladat3(beolvas)