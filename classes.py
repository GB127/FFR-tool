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
                                        "Armors" : ["Cloth"],
                                        "Bracelets": ["Copper", "Silver", "Gold", "Opal"],
                                        "Shields" : ["ProCape"],
                                        "Helmets" : ["Cap", "Ribbon"],
                                        "Gauntlets" : ["Gloves", "ProRing"]
                                        },
                            "Weapons": {"Swords" : [],
                                        "Axes" : None,
                                        "Daggers" : ["Small", "Large", "Silver"],
                                        "Staffs" : ["Wooden", "Power", "Mage"],
                                        "Hammers" : None,
                                        "Nunchucks" : None,
                                        "Others" : ["Masmune"]},
                            }




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