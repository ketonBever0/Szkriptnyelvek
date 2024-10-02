# Nev: Kurucz László
# Neptun: Z5RFY1
# h: h373677


def nyertes_korok(adam, ellenfel):
    if len(adam) != len(ellenfel) or len(adam) == 0 and len(ellenfel) == 0: return -1

    adam_nyert = 0

    for i in range(len(adam)):
        if(adam[i] > ellenfel[i]): adam_nyert += 1

    return adam_nyert

# print(nyertes_korok([], []))