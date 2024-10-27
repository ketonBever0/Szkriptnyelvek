
szamok = []
with open("alma.txt", "r") as file:
    sor = file.readline()
    while(sor):
        szamok.append(sor.strip())
        sor = file.readline()

print(szamok)


with open("./valami.txt", "w") as file:
    for i in range(10, 50, 2):
        file.write(f"{i}\n")