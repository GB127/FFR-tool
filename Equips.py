class weapon:
    def __init__(self,cat, name, D, H):
        self.cat = cat
        self.name = name
        self.H = H
        self.D = D
    def __str__(self):
        return " ".join([self.cat, self.name, str(self.H), str(self.D)])


    def canequip(self,c1,c2,c3,c4):
        if any([self.name in x.canequip["Weapons"][self.cat] for x in [c1,c2,c3,c4]]):
            return True

    def __lt__(self, other):
        if self.D < other.D:
            return True
        elif self.D > other.D:
            return False
        elif self.H < other.H:
            return True

