l0 = [0, 1, 4, 5]

for i in l0:
    print(i)

l0[1] = 10
print(l0)

def atalakit(lista):
    for i in lista:
        i = i.upper
    return lista

lista = ["Karoly", "Alma", "Laszlo"]

print(" ".join(lista))


dict = {
    "nev": "László",
    "kor": 24
}

for i in dict.values():
    print(i)

for k, v in dict.items():
    print(f"{k}: {v}")

