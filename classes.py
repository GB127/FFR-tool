class FFRError(BaseException):
    pass  # We'll see
class FFRclasses:
    def __init__(self):
        self.canequip = {}
        self.acro = "XX"
        self.equiped = []

    def equips(self, wearmor):
        self.equiped.append(wearmor)

    def checkequip(self,WA,cat,name, string=False):
        if name in self.canequip[WA][cat]: return "X"
        else : 
            if string: return "-"
            return False
    def getacro(self):
        return self.acro

class Fighter(FFRclasses):
    def __init__(self):
        self.equiped = []
        self.acro = "Fi"
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden", "Chain", "Iron", "Silver", "Steel", "Ice", "Flame"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Wooden", "iron", "Silver", "Buckler", "Flame", "Ice", "Procape"],
                                    "Helmets" : ["Cap", "Wooden", "Iron", "Silver", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "Cooper", "Iron", "Silver","Power", "ProRing"]
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
        self.canequip["Armory"]["Armor"].append("Opal")
        self.canequip["Armory"]["Armor"].append("Dragon")
        self.canequip["Armory"]["Shields"].append("Opal")
        self.canequip["Armory"]["Shields"].append("Aegis")
        self.canequip["Armory"]["Helmets"].append("Heal")
        self.canequip["Armory"]["Helmets"].append("Opal")
        self.canequip["Armory"]["Gauntlets"].append("Zeus")
        self.canequip["Armory"]["Gauntlets"].append("Opal")
        self.canequip["Weapons"]["Swords"].append("Bane")
        self.canequip["Weapons"]["Hammer"].append("Thor")
        self.canequip["Weapons"]["Others"] = ["Rapier", "Scimtar", "Sabre", "Falchon","Vorpal", "Catclaw", "Defense","Xcalber", "Masmune"]

class Thief(FFRclasses):
    def __init__(self):
        self.acro = "Th"
        self.equiped = []
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Buckler", "Procape"],
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
                            "Shields" : ["Wooden", "iron", "Silver", "Buckler", "Flame", "Ice", "Procape"],
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
        self.equiped = []
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
        self.equiped = []
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Procape"],
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
        self.canequip["Armory"]["Armor"].append("White Shrit")

class BlackMage(FFRclasses):
    def __init__(self):
        self.acro = "BM"
        self.equiped = []
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
            self.equiped = []
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