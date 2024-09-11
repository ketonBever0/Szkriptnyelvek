import math

def bor_mennyiseg(vendegek):

    liter = vendegek * 450
    return math.ceil(liter / 750)


vendeg_szam = int(input("Vendégek száma: "))

print(bor_mennyiseg(vendeg_szam))


def konyvespolc(malacka_konyvei):
    return math.ceil(malacka_konyvei / 20)


malacka = int(input("Malacka könyvei: "))
print(konyvespolc(malacka))
