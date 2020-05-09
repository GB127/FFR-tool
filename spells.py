class spell:
    def __init__(self,acro, name, target, effect):
        self.acro = acro
        self.name = name
        self.target = target
        self.effect = effect
    def __lt__(self, other):
        #if self.acro[:-1] == other.acro[:-1] : return self.acro[:-1] < other.acro[:-1]
        #return self.acro < other.acro
        return self.name < other.name
    def __str__(self):
        return f'{self.acro:^6}|{self.name:<14}|{self.target:<12}|{self.effect}'

ListWhites = [
    spell("Cure", "Cure", "1 ally", "Heal X HP "),
    spell("Harm", "Harm", "All enemies", "Hurts Undeads (20-80 HP)"),
    spell("Fog", "Fog", "Caster", "Armor +8"),
    spell("Ruse", "Ruse", "Caster", "Evade + 40%"),
    spell("Lamp", "Lamp", "1 ally", "Remove Dark status"),
    spell("Mute", "Mute", "1 enemy", "??????"),
    spell("Alit", "Anti-lighting", "Party", "Reduces lighting damage 25-50%"),
    spell("Invs", "Invisible", "1 ally", "Evade +20%"),
    spell("Cur2", "Cure 2", "1 ally", "Heal 32-64HP"),
    spell("Hrm2", "Harm 2", "All enemies", "Hurts Undeads (40-160 HP)"),
    spell("Afir", "Anti-fire", "Party", "Reduces fire damage 25-50%"),
    spell("Heal", "Heal", "Party", "Heal 12-24 HP"),
    spell("Pure", "Pure", "1 ally", "Cure poison"),
    spell("Fear", "Fear", "All enemies", "Increase Enemies' chance to flee"),
    spell("Aice", "Anti-ice", "Party", "Reduces ice damage 25-50%"),
    spell("Amut", "Anti-mute", "1 ally", "Nullify mute status" ),
    spell("Cur3", "Cure 3", "1 ally", "Heal 64-128 HP"),
    spell("Life", "Life", "1 ally", "Revive a slain ally (1 HP)"),
    spell("Hrm3", "Harm 3", "All enemies", "Damages Undeads 60-240 HP"),
    spell("Hel2", "Heal 2", "Party", "Heal 24-48 HP"),
    spell("Soft", "Soft", "1 ally", "Cure Stone status"),
    spell("Exit", "Exit", "Party", "Exit the dungeon"),
    spell("Fog2", "Fog 2", "Party", "Armor +12"),
    spell("Inv2", "Invisible 2", "Party", "Evade + 40%"),
    spell("Cur4", "Cure 4", "1 ally", "Heal max HP"),
    spell("Hrm4", "Harm 4", "All enemies", "Damage undeads 80-320 HP"),
    spell("Arub", "Anti Rub", "Party", "Protects from RUB spells"),
    spell("Hel3", "Heal 3", "Party", "Heal 48-96 HP"),
    spell("Fade", "Fade", "All enemies", "Damage enemies XX HP"),
    spell("Wall", "Wall", "1 ally", "Protects from enemies' magic"),
    spell("Xfer", "Xfer", "1 enemy", "?????"),
    spell("Lif2", "Life 2","1 ally", "Revives a slain ally (max HP)")]



ListBlacks = []
"""
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(
spell(







]"""


if __name__ == "__main__":
    ListWhites.sort()
    for i in ListWhites: print(i)