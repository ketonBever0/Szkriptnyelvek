class Telefon():
    def __init__(self, telefonszam, szin = "fekete"):
        self._telefonszam = telefonszam
        self.szin = szin
        self.tartozek = []
        
        @property
        def telefonszam(self):
            return self.telefonszam
        
        @telefonszam.setter
        def telefonszam(self, szam):
            self._telefonszam = szam

        def __str__(self):
            return f"{self.telefonszam}, {self.szin}, {', '.join(self.tartozek)}"

        def tartozekot_vesz(self, t):
            self.tartozek.append(t)

        def __add__(self, other):
            if isinstance(other, Telefon):
                return Telefon(self.telefonszam, other.szin)


t = Telefon("+361241352321")
t.tartozekot_vesz("tok")
t.tartozekot_vesz("töltő")
print(t)
