def lakoma():
    teljes = {
        "fej": input(),
        "test": input(),
        "kar": input() * 2,
        "lab": input() * 2
    }
    return max(teljes, key = teljes.get)
# print(lakoma())