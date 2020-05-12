class equipableitem:
    def __init__(self, cat, name):
        self.cat = cat
        self.name = name
    def __lt__(self, other):
        if self.cat != other.cat : return self.cat < other.cat
        else: return self.name < other.name


class armor(equipableitem):
    def __init__(self,cat, name, A, E):
        super().__init__(cat,name)
        self.A = A  # Absorb hits
        self.E = E  # Evasions (Always negative)
    def __str__(self):
        return f"{self.cat:<12}|{self.name:<10}|{str(self.A):^4}|{str(self.E):^4}|"
    def isbetter(self,other):
        return any([self.A > other.A])

class weapon(equipableitem):
    def __init__(self,cat, name, D, H):
        super().__init__(cat,name)
        self.H = H  # Hit rate
        self.D = D  # Damage
    def __str__(self):
        return f"{self.cat:<12}|{self.name:<10}|{str(self.D):^4}|{str(self.H):^4}|"
    def isbetter(self,other):
        return any([self.H > other.H, self.D > other.D])

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



def updateliste(listWA,characters):  # Ok
    """ Function that take a list of armor or weapon and a list of characters
        and returns an updated list that removes items that can't be equiped by 
        the whole team.

        Arguments:
            liste (list) : uniform List of weapons or armors to be updated.
            characters (list) : List of the characters in the team
    """
    listcan = []
    for item in listWA :
        if any([char.checkequip(item) for char in characters]):
            listcan.append(item)
    listcan.sort()
    return listcan




if __name__ == "__main__":
    test = armor("Axe", "Prune", 5,5)
    test2 = armor("Axe", "Orange",7,5)
    test3 = armor("Axe", "Prune", 3,7)

    print(test3.isbetter(test))