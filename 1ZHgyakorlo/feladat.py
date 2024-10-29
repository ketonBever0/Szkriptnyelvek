# Nev: Kurucz László
# Neptun: Z5RFY1
# h: h373677

def utolso_x_szo(txt: str, num: int):
    if txt is not txt or '!' in txt or '.' in txt or ',' in txt or '?' in txt or num <= 0:
        return "-"

    words: list[txt] = txt.split()
    if len(words) < num:
        return "-"

    # print(words)

    words.reverse()
    new_str = ""
    for i in reversed(range(0, num)):
        new_str += f"{words[i]} "

    new_str = new_str.capitalize().strip()
    new_str += '.'
    return new_str


# print(utolso_x_szo('én       vagyok a legnagyobb   rajongód', 5))


def karakter_modusz(txt: str):
    if txt is not txt or txt == "" or "uwu" in txt:
        return {'hibas': -1}

    cdict: dict[txt, int] = {}
    for char in txt:
        if char == " " or char == "\n": continue

        if char not in cdict:
            cdict[char] = 0
        cdict[char] += 1

    maxchar = 'a'
    maxnum = 0
    for key, value in cdict.items():
        if value > maxnum:
            maxnum = value
            maxchar = key

    return {maxchar: maxnum}


# print(karakter_modusz("mondtam,         fuss el, szedd a lábad, jól       elbújtál, nem \ntalállak       \n"))


class Cipo:
    def __init__(self, marka: str, meret: int, _ar=10000):
        self.marka = marka
        self.meret = meret
        self._ar = _ar if _ar > 0 else 10000
        self.matricak = []
        self.eredeti_nevek = []

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, val):
        if val is not int:
            raise ValueError("Hibas ertek!")
        self._ar = val if val > 0 else 10000

    def matrica_hozzaadas(self, mit: str):
        if not isinstance(mit, str):
            raise ValueError("Hibas matrica!")

        new_str = ""
        for i in range(0, len(mit)):
            if i % 2 == 0:
                new_str += mit[i]

        if new_str not in self.matricak:
            self.matricak.append(new_str)
            self.eredeti_nevek.append(mit)

    def __str__(self):
        if len(self.eredeti_nevek) > 0:
            txt = f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft. {len(self.eredeti_nevek)}\nNev szerint: "
            for i in range(0, len(self.eredeti_nevek)):
                txt += self.eredeti_nevek[i]
                txt += ", " if i != len(self.eredeti_nevek) - 1 else "."
            return txt
        else:
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft es meg se lett sertve matricakkal."

    def __iadd__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")

        for matrica in other.eredeti_nevek:
            self.matrica_hozzaadas(matrica)

        self.ar += (other.ar * 0.7).__round__()

        return self

    def __eq__(self, other):
        if not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        return self.marka == other.marka and self.ar == other.ar

# egy_cipo = Cipo("Nike", 35, 5000)
# egy_masik_cipo = Cipo("Adidas", 36, 5005)
# egy_cipo.ar = -1
# egy_cipo.matrica_hozzaadas("UNREAL")
# egy_masik_cipo.matrica_hozzaadas("Valami")
# egy_masik_cipo.matrica_hozzaadas("Kekw")
# print(egy_masik_cipo.matricak)
# egy_cipo += egy_masik_cipo
# print(egy_cipo)
# # Az uj Nike markaju cipo, EU 35 meretu cipo ara jelenleg 13503 Ft. 2 db matrica van rajta.
# # Nev szerint: Valami, Kekw.
# print(egy_cipo == egy_masik_cipo)  # False
