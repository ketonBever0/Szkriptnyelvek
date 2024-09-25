szam = 5

if szam < 5:
    print("< 5")
elif szam == 5:
    print("5")
else:
    print("> 5")

    print("\n")

for i in range(1, 5):
    print(i)

def hello(nev = "User"):
    print(f"Hello {nev}!")

hello("Karoly")
hello()


szoveg = "Alma"
print(len(szoveg))
print(szoveg[-2])
print(szoveg[2:4])
print(szoveg[::-1])

# szoveg.replace("a")

