class weapon:
    def __init__(self,cat, name, D, H):
        self.WA = "Weapons"
        self.cat = cat
        self.name = name
        self.H = H
        self.D = D
    def __str__(self):
        return " ".join([self.cat, self.name, str(self.H), str(self.D)])

    def __lt__(self, other):
        if self.D < other.D:
            return True
        elif self.D > other.D:
            return False
        elif self.H < other.H:
            return True

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