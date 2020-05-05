class FFRError(BaseException):
    pass

class FFRclasses:
    def __init__(self):
        self.equip = {}
        self.canequip = {}
        raise FFRError("You cannot create an unamed class")

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
    def __init__(self):
        super().__init__()
        self.canequip["Armory"]["Armors"].append("Blck Shrt")
        self.canequip["Weapons"]["Staffs"].append("Wizard")
        self.canequip["Weapons"]["Others"].append("Catclaw")