import random
jatekos = int(input("Kő (1) Papír (2) Olló (3): "))
if(jatekos not in [1, 2, 3]):
    print("Érvénytelen!")
else:
    gep = random.randint(1, 3)
    print(f"Gép: {gep}")
    if jatekos == gep:
        print("Döntetlen!")
    elif (jatekos - gep) % 3 == 1:
        print("Nyertél!")
    else:
        print("Gép nyert!")