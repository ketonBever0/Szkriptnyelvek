jatek = [
    {
        'Tamas': {
            'eldobott_hogolyok': 4,
            'talalt': 1
        },
        'Ferenc': {
            'eldobott_hogolyok': 16,
            'talalt': 6,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 28,
        }
        },
        {
        'Tamas': {
            'eldobott_hogolyok': 2,
            'talalt': 2
        },
        'Ferenc': {
            'eldobott_hogolyok': 3,
            'talalt': 2,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 4,
            'talalt': 2,
            'fejtalalat': 1
        }
    }
]

statok = hogolyo_csata(jatek)

pontossagok = hogolyo_pontossag(statok)
pontossagok2 = {
    "Geza": {
        "eldobott_hogolyok": 14,
        "talalt": 4,
        "fejtalalat": 0,
        "pontossag": 0.2857142857142857
    },
    "Lajos": {
        "eldobott_hogolyok": 45,
        "talalt": 36,
        "fejtalalat": 22,
        "pontossag": 0.8
    },
    "Jozsef": {
        "eldobott_hogolyok": 37,
        "talalt": 29,
        "fejtalalat": 15,
        "pontossag": 0.7837837837837838
    }
}
print(pontossagok)
print(hogolyo_piros_lap(pontossagok2))