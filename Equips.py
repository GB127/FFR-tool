class armor:
    def __init__(self,cat, name, A, E):
        self.cat = cat
        self.name = name
        self.A = A
        self.E = E
    def __str__(self):
        return " ".join([self.cat, self.name, str(self.A), str(self.E)])

    def __lt__(self, other):
        if self.cat < other.cat : return True
        elif self.name < other.name : return True

    def isbetter(self,other):
        if self.A < other.A:
            return True
        elif self.A > other.A:
            return False
class weapon:
    def __init__(self,cat, name, D, H):
        self.cat = cat
        self.name = name
        self.H = H
        self.D = D
    def __str__(self):
        return " ".join([self.cat, self.name, str(self.H), str(self.D)])

    def __lt__(self, other):
        if self.cat < other.cat : return True
        elif self.name < other.name : return True

    def isbetter(self,other):
        if self.D < other.D:
            return True
        elif self.D > other.D:
            return False
        elif self.H < other.H:
            return True




listarmors = [
    armor("Armors","Cloth",1,-2),
    armor("Armors","Wooden",4,-5),
    armor("Armors","Chain",15,-15),
    armor("Armors","Iron",24,-23),
    armor("Armors","Silver",18,-8),
    armor("Armors","Steel",34,-33),
    armor("Armors","Ice",34,-10),
    armor("Armors","Flame",34,-10),
    armor("Armors","Opal",42,-10),
    armor("Armors","Dragon",42,-10),
    armor("Armors","Blck Shrt",24,-2),
    armor("Armors","Wht Shrt",24,-2),

    armor("Bracelets","Copper",4,-1),
    armor("Bracelets","Silver",15,-1),
    armor("Bracelets","Gold",24,-1),
    armor("Bracelets","Opal",36,-1),

    armor("Shields","Wooden",2,0),
    armor("Shields","Iron",4,0),
    armor("Shields","Silver",8,0),
    armor("Shields","Buckler",2,0),
    armor("Shields","Flame",12,0),
    armor("Shields","Ice",12,0),
    armor("Shields","Opal",16,0),
    armor("Shields","Aegis",16,0),
    armor("Shields","ProCape",8,-2),

    armor("Helmets","Cap",1,-1),
    armor("Helmets","Wooden",3,-3),
    armor("Helmets","Iron",5,-5),
    armor("Helmets","Silver",6,-3),
    armor("Helmets","Heal",6,-3),
    armor("Helmets","Opal",8,-3),
    armor("Helmets","Ribbon",1,-1),

    armor("Gauntlets","Gloves",1,-1),
    armor("Gauntlets","Copper",2,-3),
    armor("Gauntlets","Iron",4,-5),
    armor("Gauntlets","Silver",6,-3),
    armor("Gauntlets","Zeus",6,-3),
    armor("Gauntlets","Power",6,-3),
    armor("Gauntlets","Opal",8,-3),
    armor("Gauntlets","ProRing",8,-1)]

listweapons = [
    weapon("Swords","Short",15,10),
    weapon("Swords","Rune",18,15),
    weapon("Swords","Were",18,15),
    weapon("Swords","Dragon",19,15),
    weapon("Swords","Coral",19,15),
    weapon("Swords","Long",20,10),
    weapon("Swords","Silver",23,15),
    weapon("Swords","Giant",21,20),
    weapon("Swords","Bane",22,20),
    weapon("Swords","Flame",26,20),
    weapon("Swords","Ice",29,25),
    weapon("Swords","Sun",32,30),
    weapon("Axes","Hand",16,5),
    weapon("Axes","Great",22,5),
    weapon("Axes","Silver",25,10),
    weapon("Axes","Light",28,15),

    weapon("Daggers","Small",5,10),
    weapon("Daggers","Large",7,10),
    weapon("Daggers","Silver",10,15),

    weapon("Staffs","Wooden",6, 0),
    weapon("Staffs","Power",12,0),
    weapon("Staffs","Iron",14,0),
    weapon("Staffs","Heal",6,0),
    weapon("Staffs","Mage",12,10),
    weapon("Staffs","Wizard",15,15),

    weapon("Hammers","Iron",9,0),
    weapon("Hammers","Silver",12,5),
    weapon("Hammers","Thor",18,15),
    weapon("Nunchucks","Wooden",12,0),
    weapon("Nunchucks","Iron",16,0),
    weapon("Others","Rapier",9,5),
    weapon("Others","Scimtar",10,10),
    weapon("Others","Sabre",13,5),
    weapon("Others","Falchon",15,10),
    weapon("Others","Vorpal",24,25),
    weapon("Others","Catclaw",22,35),
    weapon("Others","Defense",30,35),
    weapon("Others","Katana",33,35),
    weapon("Others","Xcalber",45,35),
    weapon("Others","Masmune",56,50)]