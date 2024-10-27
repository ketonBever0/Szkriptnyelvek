with open("alma.txt", "r") as file:
    while(sor):
        sor = file.readline()
        szamok.append(sor.strip())