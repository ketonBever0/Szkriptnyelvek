class Stadion:
    def __init__(self, team: str, fdcouk: str, city: str, name: str, capacity: int, lat: float, long: float,
                 country: str) -> None:
        self.team = team
        self.fdcouk = fdcouk
        self.city = city
        self.name = name
        self.capacity = capacity
        self.lat = lat
        self.long = long
        self.country = country


stadions: list[Stadion] = []


def readfile(path: str) -> None:
    try:
        with open(path, "r", encoding="utf-8") as csvfile:
            next(csvfile)
            stadions.clear()
            for line in csvfile:
                row = line.strip().split(",")
                stadions.append(
                    Stadion(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), int(row[4]), float(row[5]),
                            float(row[6]), row[7].strip()))
    except:
        return


def legnagyobb_stadion(path) -> None:
    readfile(path)
    with open("legnagyobb.txt", "w", encoding="utf-8") as wfile:
        if len(stadions) == 0:
            wfile.write("Nincs (Nincs)\n")
        else:
            max_capacity = stadions[0]
            for stadion in stadions:
                if stadion.capacity > max_capacity.capacity: max_capacity = stadion
            if max_capacity == 0:
                wfile.write("Nincs (Nincs)\n")
            else:
                wfile.write(f"{max_capacity.name} ({max_capacity.city})\n")


def osszes_arena(path) -> None:
    readfile(path)
    with open("./arena_park.csv", "w", encoding="utf-8") as wfile:
        wfile.write("Stadium,City,Country,Big\n")
        for stadion in stadions:
            if stadion.name.endswith("Arena"):
                wfile.write(
                    f"{stadion.name},{stadion.city},{stadion.country},{'True' if stadion.capacity > 50000 else 'False'}\n")


def osszes_park(path):
    readfile(path)
    with open("./arena_park.csv", "a", encoding="utf-8") as wfile:
        for stadion in stadions:
            if stadion.name.endswith("Park"):
                wfile.write(
                    f"{stadion.name},{stadion.city},{stadion.country},{'True' if stadion.capacity > 20000 else 'False'}\n")


def varosok_szama(path, *args):
    countries = list(args)
    if len(countries) == 0: raise Exception("Nincs megadva egy orszag sem!")
    countries.sort()

    readfile(path)
    with open("./varosok.txt", "w", encoding="utf-8") as wfile:
        grouped: dict[str, list[str]] = {}
        for stadion in stadions:
            if stadion.country in countries:
                if stadion.country not in grouped:
                    grouped[stadion.country] = []
                if stadion.city not in grouped[stadion.country]:
                    grouped[stadion.country].append(stadion.city)
                grouped[stadion.country].sort()

        for country, cities in grouped.items():
            wfile.write(f"{country} varosai:\n")
            for city in cities:
                wfile.write(f"\t{city}\n")
            wfile.write("----------\n")

# legnagyobb_stadion("./stadium.csv")
# osszes_arena("./stadium.csv")
# osszes_park("./stadium.csv")
# varosok_szama("./stadium.csv", "Spain", "Germany", "Hungary")
