class Palack:
    def __init__(self, ital: str | None, max_urtartalom: int, jelenlegi_urtartalom: int = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = max_urtartalom if jelenlegi_urtartalom > max_urtartalom else jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, ertek):
        if ertek > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        elif ertek == 0:
            self.ital = None
            self._jelenlegi_urtartalom = 0
        else:
            self._jelenlegi_urtartalom = ertek

    def suly(self):
        return self.max_urtartalom / 35 + self._jelenlegi_urtartalom

    def __str__(self) -> str:
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other) -> bool:
        return (isinstance(self, Palack) and isinstance(other, Palack)) and (
                    self.ital is not None and other.ital is not None) and self.ital == other.ital and self.max_urtartalom == other.max_urtartalom and self.jelenlegi_urtartalom == other.jelenlegi_urtartalom

    def __iadd__(self, other):
        if (not isinstance(self, Palack) and not isinstance(other, Palack)) or (self.ital is None or other.ital is None) or self == other or self.jelenlegi_urtartalom >= self.max_urtartalom: return self

        mennyit = min(other.jelenlegi_urtartalom, self.max_urtartalom - self.jelenlegi_urtartalom)
        self.jelenlegi_urtartalom += mennyit
        other.jelenlegi_urtartalom -= mennyit
        if self.ital is None:
            self.ital = other.ital
        elif other.ital != self.ital:
            self.ital = "keverek"
        return self


class VisszavalthatoPalack(Palack):
    def __init__(self, ital: str | None, max_urtartalom: int, jelenlegi_urtartalom: int = 1, palackdij: int = 25):
        super().__init__(ital, max_urtartalom, jelenlegi_urtartalom)
        self.palackdij = palackdij

    def __str__(self):
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self.jelenlegi_urtartalom} ml van benne, maximum {super().max_urtartalom} ml fer bele."


class Rekesz:
    def __init__(self, max_teherbiras: int):
        self.max_teherbiras = max_teherbiras
        self.palackok: list[Palack | VisszavalthatoPalack] = []

    def suly(self):
        if len(self.palackok) == 0: return 0
        suly = 0
        for palack in self.palackok:
            suly += palack.suly()
        return suly

    def uj_palack(self, palack: Palack | VisszavalthatoPalack):
        if self.max_teherbiras > self.suly() + palack.suly(): self.palackok.append(palack)

    def osszes_penz(self):
        osszes = 0
        for palack in self.palackok:
            if isinstance(palack, VisszavalthatoPalack): osszes += palack.palackdij
        return osszes

# pia1 = Palack("Narancs", 50, 10)
# pia2 = Palack("Narancs", 50, 49)

# pia3 = Palack("Dreher", 40, 30)
# print(pia3)

# pia3 += pia1
#
# print(pia3)

# v_pia1 = VisszavalthatoPalack("Kóla", 40, 30)
# v_pia2 = VisszavalthatoPalack("Kóla", 40, 30, 50)

# rekesz = Rekesz(1000)
# rekesz.uj_palack(pia2)
# rekesz.uj_palack(v_pia1)
# rekesz.uj_palack(v_pia2)

# print(rekesz.suly())
# print(rekesz.osszes_penz())
