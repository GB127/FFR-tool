from Equips import weapon, armor, listarmors, listweapons

class FFRError(BaseException):
    pass  # We'll see
class FFRclasses:
    """ Grandfather of classes. This encapsulates all methods that are
        shared between all classes. Can't be used since it doesn't have
        a self.canequip that isn't empty.
    

        Datas of all the classes:
            acro (str) : String of two characters that identidy the class.
            canequip : Dicto of everything that the class can equip.

        Methods of all classes:
            checkequip: Checks if said class can equip the item provided.

    
    """
    def __init__(self):
        self.canequip = []
        self.acro = "XX"

    def checkequip(self,WA, string=False):
        if WA in self.canequip: 
            print("allo")
            return "X"
        else : 
            if string: return "-"
            return False

class Fighter(FFRclasses):
    def __init__(self):
        self.acro = "Fi"
        self.canequip = [listarmors[0],listarmors[1],listarmors[2],listarmors[3],listarmors[4], listarmors[5],listarmors[6],listarmors[7],listarmors[12],listarmors[13], listarmors[14],listarmors[15],listarmors[16],listarmors[17],listarmors[18],listarmors[19],listarmors[20],listarmors[21],listarmors[24],listarmors[25],listarmors[26],listarmors[27],listarmors[28],listarmors[31],listarmors[32],listarmors[33],listarmors[34],listarmors[35],listarmors[37],listarmors[39],
                        listweapons[0], listweapons[1], listweapons[2], listweapons[3],listweapons[4], listweapons[5], listweapons[6], listweapons[7], listweapons[9], listweapons[10], listweapons[11], listweapons[12], listweapons[13], listweapons[14], listweapons[15], listweapons[16], listweapons[17], listweapons[18], listweapons[19], listweapons[20], listweapons[21], listweapons[25], listweapons[26], listweapons[30], listweapons[31], listweapons[32], listweapons[33],listweapons[39]]

class Knight(Fighter):
    def __init__(self):
        super().__init__()
        self.acro = "Kn"
        self.canequip += [
            listarmors[8],
            listarmors[9],
            listarmors[22],
            listarmors[23],
            listarmors[29],
            listarmors[30],
            listarmors[36],
            listarmors[38],
            listweapons[8],
            listweapons[27],
            listweapons[34],
            listweapons[35],
            listweapons[36],
            listweapons[38]]


class Thief(FFRclasses):
    def __init__(self):
        self.acro = "Th"
        self.canequip = [
            listarmors[0],
            listarmors[1],
            listarmors[4],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[19],
            listarmors[24],
            listarmors[25],
            listarmors[31],
            listarmors[32],
            listarmors[39],
            listweapons[1],
            listweapons[3],
            listweapons[4],
            listweapons[16],
            listweapons[17],
            listweapons[18],
            listweapons[30],
            listweapons[31],
            listweapons[32],
            listweapons[33],
            listweapons[39]]

class Ninja(Thief):
    def __init__(self):
        self.acro = "Ni"
        self.canequip = {
                "Armory" : {
                            "Armors" : ["Cloth", "Wooden", "Chain", "Iron", "Silver", "Ice", "Flame"],
                            "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                            "Shields" : ["Wooden", "Iron", "Silver", "Buckler", "Flame", "Ice", "ProCape"],
                            "Helmets" : ["Cap", "Wooden", "Iron", "Silver","Heal", "Ribbon"],
                            "Gauntlets" : ["Gloves", "Cooper", "Iron", "Silver", "Zeus", "Power", "ProRing"]
                            },
                "Weapons": {"Swords" : ["Short","Were", "Rune", "Dragon", "Coral", "Long", "Silver", "Giant","Bane", "Flame", "Ice", "Sun"],
                            "Axes" : ["Hand", "Great", "Silver", "Light"],
                            "Daggers" : ["Small", "Large", "Silver"],
                            "Staffs" : ["Wooden","Power", "Iron", "Heal", "Mage"],
                            "Hammers" : ["Iron", "Silver", "Thor"],
                            "Nunchucks" : ["Wooden", "Iron"],
                            "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon","Vorpal", "Catclaw", "Defense", "Katana", "Masmune"]},
                }
class BlackBelt(FFRclasses):
    def __init__(self):
        self.acro = "BB"
        self.canequip = [
            listweapons[19],
            listweapons[20],
            listweapons[28],
            listweapons[29],
            listweapons[39],
            listarmors[0],
            listarmors[1],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[25],
            listarmors[31],
            listarmors[32],
            listarmors[39]]

class Master(BlackBelt):
    def __init__(self):
        super().__init__()
        self.acro = "Ma"
        
        self.canequip.append(listweapons[21])
class WhiteMage(FFRclasses):
    def __init__(self):
        self.acro = "WM"
        self.canequip = [
            listarmors[0],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[24],
            listarmors[25],
            listarmors[31],
            listarmors[32],
            listarmors[39],
            listweapons[19],
            listweapons[20],
            listweapons[22],
            listweapons[25],
            listweapons[26],
            listweapons[39]]


class WhiteWizard(WhiteMage):
    def __init__(self):
        super().__init__()
        self.acro = "WW"
        self.canequip.append(listweapons[27])
        self.canequip.append(listarmors[11])

class BlackMage(FFRclasses):
    def __init__(self):
        self.acro = "BM"

        self.canequip = [
            listarmors[0],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[24],
            listarmors[25],
            listarmors[31],
            listweapons[16],
            listweapons[17],
            listweapons[18],
            listweapons[19],
            listweapons[20],
            listweapons[23],
            listweapons[39]]

class BlackWizard(BlackMage):
    def __init__(self):
        super().__init__()
        self.acro = "BW"
        self.canequip.append(listarmors[10])
        self.canequip.append(listweapons[24])
        self.canequip.append(listweapons[35])
class RedMage(FFRclasses):
        def __init__(self):
            self.acro = "RM"

            self.canequip = [
                armor("Armors","Cloth",1,-2),
                armor("Armors","Wooden",4,-5),
                armor("Armors","Chain",15,-15),
                armor("Armors","Silver",18,-8),
                armor("Bracelets","Copper",4,-1),
                armor("Bracelets","Silver",15,-1),
                armor("Bracelets","Gold",24,-1),
                armor("Bracelets","Opal",36,-1),
                armor("Shields","Buckler",2,0),
                armor("Helmets","Cap",1,-1),
                armor("Helmets","Ribbon",1,-1),
                armor("Gauntlets","Gloves",1,-1),
                armor("Gauntlets","ProRing",8,-1),
                weapon("Swords","Short",15,10),
                weapon("Swords","Rune",18,15),
                weapon("Swords","Dragon",19,15),
                weapon("Swords","Coral",19,15),
                weapon("Swords","Long",20,10),
                weapon("Swords","Silver",23,15),
                weapon("Swords","Giant",21,20),
                weapon("Swords","Flame",26,20),
                weapon("Swords","Ice",29,25),
                weapon("Swords","Sun",32,30),
                weapon("Daggers","Small",5,10),
                weapon("Daggers","Large",7,10),
                weapon("Daggers","Silver",10,15),
                weapon("Staffs","Wooden",6, 0),
                weapon("Others","Rapier",9,5),
                weapon("Others","Scimtar",10,10),
                weapon("Others","Sabre",13,5),
                weapon("Others","Falchon",15,10),
                weapon("Others","Masmune",56,50)]


class RedWizard(RedMage):
    def __init__(self):
        super().__init__()
        self.acro = "RW"
        self.canequip.append(armor("Shields","ProCape",8,-2))
        self.canequip.append(armor("Gauntlets","Silver",6,-3))
        self.canequip.append(armor("Gauntlets","Zeus",6,-3))
        self.canequip.append(armor("Gauntlets","Power",6,-3))
        self.canequip.append(weapon("Swords","Were",18,15))
        self.canequip.append(weapon("Swords","Bane",22,20))
        self.canequip.append(weapon("Others","Vorpal",24,25))
        self.canequip.append(weapon("Others","Catclaw",22,35))
        self.canequip.append(weapon("Others","Defense",30,35))