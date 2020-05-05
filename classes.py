class FFRError(BaseException):
    pass  # We'll see

class FFRclasses:
    def __init__(self):
        self.equip = {}
        self.canequip = {}

class Fighter(FFRclasses):
    def __init__(self):
        self.equip = {}
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
                                    "Nunchucks" : None,
                                    "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                        }
class Knight(Fighter):
    def __init__(self):
        super().__init__()
        # Armors TODO
        self.canequip["Weapons"]["Swords"].append("Bane")
        self.canequip["Weapons"]["Hammer"].append("Thor")
        self.canequip["Weapons"]["Others"] = ["Rapier", "Scimtar", "Sabre", "Falchon","Vorpal", "Catclaw", "Defense","Xcalber", "Masmune"]

class Thief(FFRclasses):
    def __init__(self):
        self.equip = {}
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Buckler", "Procape"],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : ["Rune", "Dragon", "Coral"],
                                    "Axes" : None,
                                    "Daggers" : ["Small", "Large", "Silver"],
                                    "Staffs" : None,
                                    "Hammers" : None,
                                    "Nunchucks" : None,
                                    "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                        }

class Ninja(Thief):
    def __init__(self):
        pass #FIXME
        # http://mikesrpgcenter.com/ffantasy/armor.html
        # http://mikesrpgcenter.com/ffantasy/weapons.html

class BlackBelt(FFRclasses):
    def __init__(self):
        self.equip = {}
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth", "Wooden"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : None,
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : None,
                                    "Axes" : None,
                                    "Daggers" : None,
                                    "Staffs" : ["Wooden", "Power"],
                                    "Hammers" : None,
                                    "Nunchucks" : ["Wooden", "Iron"],
                                    "Others" : ["Masmune"]}
                        }
class Master(BlackBelt):
    def __init__(self):
        super().__init__()
        self.canequip["Weapons"]["Staffs"].append("Iron")
class WhiteMage(FFRclasses):
    def __init__(self):
        self.equip = {}
        self.canequip = {
                        "Armory" : {
                                    "Armors" : ["Cloth"],
                                    "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                    "Shields" : ["Procape"],
                                    "Helmets" : ["Cap", "Ribbon"],
                                    "Gauntlets" : ["Gloves", "ProRing"]
                                    },
                        "Weapons": {"Swords" : None,
                                    "Axes" : None,
                                    "Daggers" : None,
                                    "Staffs" : ["Wooden","Power", "Heal"],
                                    "Hammers" : ["Iron", "Silver"],
                                    "Nunchucks" : None,
                                    "Others" : ["Masmune"]},
                        }

class WhiteWizard(WhiteMage):
    def __init__(self):
        super().__init__()
        self.canequip["Weapons"]["Hammers"].append("Thor")
        self.canequip["Armors"]["Armor"].append("White Shrit")

class BlackMage(FFRclasses):
    def __init__(self):
        self.equip = {}

        self.canequip = {
            "Armory" : {
                        "Armors" : ["Cloth"],
                        "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                        "Shields" : ["ProCape"],
                        "Helmets" : ["Cap", "Ribbon"],
                        "Gauntlets" : ["Gloves", "ProRing"]
                        },
            "Weapons": {"Swords" : None,
                        "Axes" : None,
                        "Daggers" : ["Small", "Large", "Silver"],
                        "Staffs" : ["Wooden", "Power", "Mage"],
                        "Hammers" : None,
                        "Nunchucks" : None,
                        "Others" : ["Masmune"]},
            }
class BlackWizard(BlackMage):
class RedMage(FFRclasses):
        def __init__(self):
            self.equip = {}

            self.canequip = {
                            "Armory" : {
                                        "Armors" : ["Cloth", "Wooden", "Chain", "Silver"],
                                        "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                        "Shields" : ["Buckler"],
                                        "Helmets" : ["Cap", "Ribbon"],
                                        "Gauntlets" : ["Gloves", "ProRing"]
                                        },
                            "Weapons": {"Swords" : ["Short", "Rune", "Dragon", "Coral", "Long", "Silver", "Giant", "Flame", "Ice", "Sun"],
                                        "Axes" : None,
                                        "Daggers" : ["Small", "Large", "Silver"],
                                        "Staffs" : ["Wooden"],
                                        "Hammers" : None,
                                        "Nunchucks" : None,
                                        "Others" : ["Rapier", "Scimtar", "Sabre", "Falchon", "Masmune"]},
                            }
class RedWizard(RedMage):
    def __init__(self):
        super().__init__()
        self.canequip["Armory"]["Shields"].append("ProCape")
        self.canequip["Armory"]["Gauntlets"].append("Silver")
        self.canequip["Armory"]["Gauntlets"].append("Zeus")
        self.canequip["Armory"]["Gauntlets"].append("Power")
        self.canequip["Weapons"]["Swords"].append("Were")
        self.canequip["Weapons"]["Swords"].append("Bane")
        self.canequip["Weapons"]["Others"].append("Vorpal")
        self.canequip["Weapons"]["Others"].append("Catclaw")
        self.canequip["Weapons"]["Others"].append("Defense")


    def __init__(self):
        super().__init__()
        self.canequip["Armory"]["Armors"].append("Blck Shrt")
        self.canequip["Weapons"]["Staffs"].append("Wizard")
        self.canequip["Weapons"]["Others"].append("Catclaw")