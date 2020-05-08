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
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden", "Chain", "Iron", "Silver", "Steel", "Ice", "Flame"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Wooden", "Iron", "Silver", "Buckler", "Flame", "Ice", "ProCape"],
                                    "Helmets" : ["Cap", "Wooden", "Iron", "Silver", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "Copper", "Iron", "Silver","Power", "ProRing"]
                                    },
                        "Weapons": {"Swords" : ["Short","Were", "Rune", "Dragon", "Coral", "Long", "Silver", "Giant", "Flame", "Ice", "Sun"],
                                    "Axes" : ["Hand", "Great", "Silver", "Light"],
                                    "Daggers" : ["Small", "Large", "Silver"],
                                    "Staffs" : ["Wooden","Power", "Iron"],
                                    "Hammers" : ["Iron", "Silver"],
                                    "Nunchucks" : [],
                                    "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                        }
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