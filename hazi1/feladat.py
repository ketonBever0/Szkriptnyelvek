# Nev: Kurucz László
# Neptun: Z5RFY1
# h: h373677

def szekem(jegy):
    return f"{jegy // 14 if jegy % 14 == 0 else jegy // 14 + 1}. sor, {"bal" if jegy % 14 > 7 or jegy % 14 == 0 else "jobb"} {(7 if jegy % 7 == 0 else jegy % 7) if ("bal" if jegy % 14 > 7 or jegy % 14 == 0 else "jobb") == "bal" else 7 - (7 if jegy % 7 == 0 else jegy % 7) + 1}. szek"

def szekem_hosszu(jegy):

    sor = jegy // 14 if jegy % 14 == 0 else jegy // 14 + 1
    oldal = "bal" if jegy % 14 > 7 or jegy % 14 == 0 else "jobb"
    hely = 7 if jegy % 7 == 0 else jegy % 7
    szam = hely if oldal == "bal" else 7 - hely + 1

    return f"{sor}. sor, {oldal} {szam}. szek"


print(szekem(43))