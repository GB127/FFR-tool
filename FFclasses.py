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
        self.equiped = {"Weapon" : weapon("Unarmed", "Unarmed", 0,0),
                        "Helmet" : armor("Helmets", "Hairs", 0,0),
                        "Shield" : armor("Shields", "Elbow", 0,0),
                        "Armor" : armor("Armors", "Skin", 0,0),
                        "Gauntlets": armor("Gauntlets", "Hands", 0,0),
                        "Bracelets" : armor("Bracelets", "Wrists", 0,0)}
    def __str__(self):
        string = f'{self.__class__.__name__}\n' + "-" * 35 + "\n"
        for i in self.equiped.keys():
            string += f'{str(self.equiped[i])}\n'
        return string
    def checkequip(self,WA, string=False):
        if WA in self.canequip: 
            return "X"
        else : 
            if string: return "-"
            return False

class Fighter(FFRclasses):
    def __init__(self):
        super().__init__()
        self.acro = "Fi"
        self.canequip = [listarmors[0],listarmors[1],listarmors[2],listarmors[3],listarmors[4], listarmors[5],listarmors[6],listarmors[7],listarmors[12],listarmors[13], listarmors[14],listarmors[15],listarmors[16],listarmors[17],listarmors[18],listarmors[19],listarmors[20],listarmors[21],listarmors[24],listarmors[25],listarmors[26],listarmors[27],listarmors[28],listarmors[31],listarmors[32],listarmors[33],listarmors[34],listarmors[35],listarmors[37],listarmors[39],
                        listweapons[0], listweapons[1], listweapons[2], listweapons[3],listweapons[4], listweapons[5], listweapons[6], listweapons[7], listweapons[9], listweapons[10], listweapons[11], listweapons[12], listweapons[13], listweapons[14], listweapons[15], listweapons[16], listweapons[17], listweapons[18], listweapons[19], listweapons[20], listweapons[21], listweapons[25], listweapons[26], listweapons[30], listweapons[31], listweapons[32], listweapons[33],listweapons[39]]
    def rankup(self):
        return Knight(self.equiped)

class Knight(Fighter):
    def __init__(self, equipment):
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
        self.equiped = equipment

class Thief(FFRclasses):
    def __init__(self):
        super().__init__()
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
    def rankup(self):
        return Ninja(self.equiped)
class Ninja(Thief):
    def __init__(self, equipment):
        self.acro = "Ni"
        self.canequip = [
            listarmors[0],
            listarmors[1],
            listarmors[2],
            listarmors[3],
            listarmors[4],
            listarmors[7],
            listarmors[8],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[16],
            listarmors[17],
            listarmors[18],
            listarmors[19],
            listarmors[20],
            listarmors[21],
            listarmors[24],
            listarmors[25],
            listarmors[26],
            listarmors[27],
            listarmors[28],
            listarmors[29],
            listarmors[31],
            listarmors[32],
            listarmors[33],
            listarmors[34],
            listarmors[35],
            listarmors[36],
            listarmors[37],
            listarmors[39],
            listweapons[0],
            listweapons[2],
            listweapons[1],
            listweapons[3],
            listweapons[4],
            listweapons[5],
            listweapons[6],
            listweapons[7],
            listweapons[8],
            listweapons[9],
            listweapons[10],
            listweapons[11],
            listweapons[12],
            listweapons[13],
            listweapons[14],
            listweapons[15],
            listweapons[16],
            listweapons[17],
            listweapons[18],
            listweapons[19],
            listweapons[20],
            listweapons[21],
            listweapons[22],
            listweapons[23],
            listweapons[25],
            listweapons[26],
            listweapons[27],
            listweapons[28],
            listweapons[29],
            listweapons[30],
            listweapons[31],
            listweapons[32],
            listweapons[33],
            listweapons[34],
            listweapons[35],
            listweapons[36],
            listweapons[37],
            listweapons[39]]
        self.equiped = equipment
class BlackBelt(FFRclasses):
    def __init__(self):
        super().__init__()
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
    def rankup(self):
        return Master(self.equiped)
class Master(BlackBelt):
    def __init__(self, equipment):
        super().__init__()
        self.acro = "Ma"
        self.canequip.append(listweapons[21])
        self.equiped = equipment
class WhiteMage(FFRclasses):
    def __init__(self):
        super().__init__()
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

    def rankup(self):
        return WhiteWizard(self.equiped)
class WhiteWizard(WhiteMage):
    def __init__(self, equipment):
        super().__init__()
        self.acro = "WW"
        self.canequip.append(listweapons[27])
        self.canequip.append(listarmors[11])
        self.equiped = equipment

class BlackMage(FFRclasses):
    def __init__(self):
        super().__init__()
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
    def rankup(self):
        return BlackWizard(self.equiped)
class BlackWizard(BlackMage):
    def __init__(self,equipment):
        super().__init__()
        self.acro = "BW"
        self.canequip.append(listarmors[10])
        self.canequip.append(listweapons[24])
        self.canequip.append(listweapons[35])
        self.equiped = equipment
class RedMage(FFRclasses):
    def __init__(self):
        super().__init__()
        self.acro = "RM"
        self.canequip = [
            listweapons[0],
            listweapons[1],
            listweapons[3],
            listweapons[4],
            listweapons[5],
            listweapons[6],
            listweapons[7],
            listweapons[9],
            listweapons[10],
            listweapons[11],
            listweapons[16],
            listweapons[17],
            listweapons[18],
            listweapons[19],
            listweapons[30],
            listweapons[31],
            listweapons[32],
            listweapons[33],
            listweapons[39],
            listarmors[0],
            listarmors[1],
            listarmors[2],
            listarmors[4],
            listarmors[12],
            listarmors[13],
            listarmors[14],
            listarmors[15],
            listarmors[19],
            listarmors[25],
            listarmors[31],
            listarmors[32],
            listarmors[39]
                        ]

    def rankup(self):
        return RedWizard(self.equiped)
class RedWizard(RedMage):
    def __init__(self, equipment):
        super().__init__()
        self.acro = "RW"
        self.canequip.append(listarmors[24])
        self.canequip.append(listarmors[35])
        self.canequip.append(listarmors[36])
        self.canequip.append(listarmors[37])
        self.canequip.append(listweapons[2])
        self.canequip.append(listweapons[8])
        self.canequip.append(listweapons[34])
        self.canequip.append(listweapons[35])
        self.canequip.append(listweapons[36])
        self.equiped = equipment