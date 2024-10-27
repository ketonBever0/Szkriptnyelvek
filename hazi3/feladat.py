# Nev: Kurucz László
# Neptun: Z5RFY1
# h: h373677


def hogolyo_csata(korok):
    vege = {}

    for kor in korok:
        for tag, stat in kor.items():
            # if(tag in vege):
            #     for nev, szam in stat.items():
            #         if(nev in vege[tag]):
            #             vege[tag][nev] += szam
            #         else:
            #             vege[tag][nev] = szam
            # else:
            #     vege[tag] = {"eldobott_hogolyok": 0, "talalt": 0, "fejtalalat": 0}
            #     for nev, szam in stat.items():
            #         if(vege[tag] == nev):
            #             print(nev)
            # ^^ Ez is működik, csak nem adja hozzá a 'fejtalalatok' mezőt, ha az 0 ^^
            if(tag not in vege): vege[tag] = {"eldobott_hogolyok": 0, "talalt": 0, "fejtalalat": 0}
            if(tag in vege):
                for nev, szam in stat.items():
                    vege[tag][nev] += szam

    return vege

def hogolyo_pontossag(statok):
    for stat in statok.values():
        if(stat["eldobott_hogolyok"] > 0):
            stat["pontossag"] = stat["talalt"] / stat["eldobott_hogolyok"]
        else:
            stat["pontossag"] = 0
    return statok

def hogolyo_piros_lap(pontossagok):
    tiltva = []
    for tag, stat in pontossagok.items():
        if(stat["pontossag"] >= 0.7 and stat["fejtalalat"] > 0):
            if(stat["fejtalalat"] / stat["talalt"] > 0.5):
                tiltva.append(tag)
    return tiltva


# jatek = [
#     {
#         'Tamas': {
#             'eldobott_hogolyok': 4,
#             'talalt': 1
#         },
#         'Ferenc': {
#             'eldobott_hogolyok': 16,
#             'talalt': 6,
#             'fejtalalat': 1
#         },
#         'Csaba': {
#             'eldobott_hogolyok': 28,
#         }
#         },
#         {
#         'Tamas': {
#             'eldobott_hogolyok': 2,
#             'talalt': 2
#         },
#         'Ferenc': {
#             'eldobott_hogolyok': 3,
#             'talalt': 2,
#             'fejtalalat': 1
#         },
#         'Csaba': {
#             'eldobott_hogolyok': 4,
#             'talalt': 2,
#             'fejtalalat': 1
#         }
#     }
# ]

# statok = hogolyo_csata(jatek)

# pontossagok = hogolyo_pontossag(statok)
# pontossagok2 = {
#     "Geza": {
#         "eldobott_hogolyok": 14,
#         "talalt": 4,
#         "fejtalalat": 0,
#         "pontossag": 0.2857142857142857
#     },
#     "Lajos": {
#         "eldobott_hogolyok": 45,
#         "talalt": 36,
#         "fejtalalat": 22,
#         "pontossag": 0.8
#     },
#     "Jozsef": {
#         "eldobott_hogolyok": 37,
#         "talalt": 29,
#         "fejtalalat": 15,
#         "pontossag": 0.7837837837837838
#     }
# }
# print(pontossagok)
# print(hogolyo_piros_lap(pontossagok2))