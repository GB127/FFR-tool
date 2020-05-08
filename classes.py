from Equips import weapon, armor

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
        self.canequip = {}
        self.acro = "XX"

    def checkequip(self,WA,cat,name, string=False):
        if name in self.canequip[WA][cat]: return "X"
        else : 
            if string: return "-"
            return False

class Fighter(FFRclasses):
    def __init__(self):
        self.acro = "Fi"
        self.canequip = [
            armor("Armors","Cloth",1,-2),
            armor("Armors","Wooden",4,-5),
            armor("Armors","Chain",15,-15),
            armor("Armors","Iron",24,-23),
            armor("Armors","Silver",18,-8),
            armor("Armors","Steel",34,-33),
            armor("Armors","Ice",34,-10),
            armor("Armors","Flame",34,-10),    
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
            armor("Shields","ProCape",8,-2),
            armor("Helmets","Cap",1,-1),
            armor("Helmets","Wooden",3,-3),
            armor("Helmets","Iron",5,-5),
            armor("Helmets","Silver",6,-3),
            armor("Helmets","Ribbon",1,-1),
            armor("Gauntlets","Gloves",1,-1),
            armor("Gauntlets","Copper",2,-3),
            armor("Gauntlets","Iron",4,-5),
            armor("Gauntlets","Silver",6,-3),
            armor("Gauntlets","Power",6,-3),
            armor("Gauntlets","ProRing",8,-1),
            weapon("Swords","Short",15,10),
            weapon("Swords","Rune",18,15),
            weapon("Swords","Were",18,15),
            weapon("Swords","Dragon",19,15),
            weapon("Swords","Coral",19,15),
            weapon("Swords","Long",20,10),
            weapon("Swords","Silver",23,15),
            weapon("Swords","Giant",21,20),
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

            weapon("Hammers","Iron",9,0),
            weapon("Hammers","Silver",12,5),


            weapon("Others","Rapier",9,5),
            weapon("Others","Scimtar",10,10),
            weapon("Others","Sabre",13,5),
            weapon("Others","Falchon",15,10),
            weapon("Others","Masmune",56,50)]
class Knight(Fighter):
    def __init__(self):
        super().__init__()
        self.acro = "Kn"
        # Armors TODO
        self.canequip["Armory"]["Armors"].append("Opal")
        self.canequip["Armory"]["Armors"].append("Dragon")
        self.canequip["Armory"]["Shields"].append("Opal")
        self.canequip["Armory"]["Shields"].append("Aegis")
        self.canequip["Armory"]["Helmets"].append("Heal")
        self.canequip["Armory"]["Helmets"].append("Opal")
        self.canequip["Armory"]["Gauntlets"].append("Zeus")
        self.canequip["Armory"]["Gauntlets"].append("Opal")
        self.canequip["Weapons"]["Swords"].append("Bane")
        self.canequip["Weapons"]["Hammers"].append("Thor")
        self.canequip["Weapons"]["Others"] = ["Rapier", "Scimtar", "Sabre", "Falchon","Vorpal", "Catclaw", "Defense","Xcalber", "Masmune"]

class Thief(FFRclasses):
    def __init__(self):
        self.acro = "Th"
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Buckler", "ProCape"],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : ["Rune", "Dragon", "Coral"],
                                    "Axes" : [],
                                    "Daggers" : ["Small", "Large", "Silver"],
                                    "Staffs" : [],
                                    "Hammers" : [],
                                    "Nunchucks" : [],
                                    "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                        }

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
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : [],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : [],
                                    "Axes" : [],
                                    "Daggers" : [],
                                    "Staffs" : ["Wooden", "Power"],
                                    "Hammers" : [],
                                    "Nunchucks" : ["Wooden", "Iron"],
                                    "Others" : ["Masmune"]}
                        }
class Master(BlackBelt):
    def __init__(self):
        super().__init__()
        self.acro = "Ma"
        self.canequip["Weapons"]["Staffs"].append("Iron")
class WhiteMage(FFRclasses):
    def __init__(self):
        self.acro = "WM"
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["ProCape"],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : [],
                                    "Axes" : [],
                                    "Daggers" : [],
                                    "Staffs" : ["Wooden","Power", "Heal"],
                                    "Hammers" : ["Iron", "Silver"],
                                    "Nunchucks" : [],
                                    "Others" : ["Masmune"]},
                        }

class WhiteWizard(WhiteMage):
    def __init__(self):
        super().__init__()
        self.acro = "WW"
        self.canequip["Weapons"]["Hammers"].append("Thor")
        self.canequip["Armory"]["Armors"].append("White Shirt")

class BlackMage(FFRclasses):
    def __init__(self):
        self.acro = "BM"
        self.canequip = {
            "Armory" : {
                        "Armors" : ["Cloth"],
                        "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                        "Shields" : ["ProCape"],
                        "Helmets" : ["Cap", "Ribbon"],
                        "Gauntlets" : ["Gloves", "ProRing"]
                        },
            "Weapons": {"Swords" : [],
                        "Axes" : [],
                        "Daggers" : ["Small", "Large", "Silver"],
                        "Staffs" : ["Wooden", "Power", "Mage"],
                        "Hammers" : [],
                        "Nunchucks" : [],
                        "Others" : ["Masmune"]},
            }
class BlackWizard(BlackMage):
    def __init__(self):
        super().__init__()
        self.acro = "BW"
        self.canequip["Armory"]["Armors"].append("Blck Shrt")
        self.canequip["Weapons"]["Staffs"].append("Wizard")
        self.canequip["Weapons"]["Others"].append("Catclaw")
class RedMage(FFRclasses):
        def __init__(self):
            self.acro = "RM"
            self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden", "Chain", "Silver"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Buckler"],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : ["Short", "Rune", "Dragon", "Coral", "Long", "Silver", "Giant", "Flame", "Ice", "Sun"],
                                    "Axes" : [],
                                    "Daggers" : ["Small", "Large", "Silver"],
                                    "Staffs" : ["Wooden"],
                                    "Hammers" : [],
                                    "Nunchucks" : [],
                                    "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                        }
class RedWizard(RedMage):
    def __init__(self):
        super().__init__()
        self.acro = "RW"
        self.canequip["Armory"]["Shields"].append("ProCape")
        self.canequip["Armory"]["Gauntlets"].append("Silver")
        self.canequip["Armory"]["Gauntlets"].append("Zeus")
        self.canequip["Armory"]["Gauntlets"].append("Power")
        self.canequip["Weapons"]["Swords"].append("Were")
        self.canequip["Weapons"]["Swords"].append("Bane")
        self.canequip["Weapons"]["Others"].append("Vorpal")
        self.canequip["Weapons"]["Others"].append("Catclaw")
        self.canequip["Weapons"]["Others"].append("Defense")