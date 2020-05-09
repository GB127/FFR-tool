class spell:
    def __init__(self,acro, name, target, effect):
        self.acro = acro
        self.name = name
        self.target = target
        self.effect = effect
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return f'{self.acro:^6}|{self.name:<14}|{self.target:<12}|{self.effect}'

ListWhites = [
    spell("Cure", "Cure", "1 ally", "Heal X HP "),
    spell("Harm", "Harm", "All enemies", "Hurts Undeads (20-80 HP)"),
    spell("Fog", "Fog", "Caster", "Armor +8"),
    spell("Ruse", "Ruse", "Caster", "Evade + 40%"),
    spell("Lamp", "Lamp", "1 ally", "Remove Dark status"),
    spell("Mute", "Mute", "1 enemy", "Prevents enemies from casting spells"),
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
    spell("Wall", "Wall", "1 ally", "Gives resistances to all elements"),
    spell("Xfer", "Xfer", "1 enemy", "Eliminate Enemie's resistances"),
    spell("Lif2", "Life 2","1 ally", "Revives a slain ally (max HP)")]



ListBlacks = [
    spell("Fire", "Fire", "1 enemy", "Fire damage 10-40 HP"),
    spell("Slep", "Sleep", "1 enemy", "Sleep"),
    spell("Lock", "Lock", "1 enemy", "Enemy's evade -10%"),
    spell("Lit", "Lighting", "1 enemy", "Lighting damage 10-40 HP"),
    spell("Ice", "Ice", "1 enemy", "Ice damage 20-80 HP"),
    spell("Dark", "Dark", "All enemies", "Dark"),
    spell("Tmpr", "Temper", "1 ally", "Hit + 14"),
    spell("Slow", "Slow", "All enemies", "Reduce Hit number"),
    spell("Fir2", "Fire 2", "All enemies", "Fire damage 30-120 HP"),
    spell("Hold", "Hold", "1 enemy", "Paralysis"),
    spell("Lit2", "Lighting 2", "All enemies", "Lighting damage XX HP"),
    spell("Lok2", "Lock 2", "All enemies", "enemies' evade -10%"),
    spell("Slp2", "Sleep 2", "1 enemy", "Sleep"),
    spell("Fast", "Fast", "1 ally", "Increase Number of hits"),
    spell("Conf", "Confuse", "All enemies", "Confuses the enemies"),
    spell("Ice2", "Ice 2", "All enemies", "Ice damage 40-160 HP"),
    spell("Fir3", "Fire 3", "All enemies", "Fire damage 50-200 HP"),
    spell("Bane", "Bane", "All enemies", "Poison/stone KO"),
    spell("Warp", "Warp", "Party", "Warp to previous level of dungeon"),
    spell("Slo2", "Slow 2", "1 enemy", "Slow"),
    spell("Lit3", "Lighting 3", "All enemies", "Lighting damage 60-240 HP"),
    spell("Rub", "Rub", "1 enemy", "Death KO"),
    spell("Qake", "Quake", "all enemies", "Earth KO"),
    spell("Stun", "Stun", "1 enemy", "Stun if <300 HP"),
    spell("Ice3", "Ice 3", "All enemies", "Ice damage 70-280 HP"),
    spell("Brak", "Break", "1 enemy", "Stone an enemy"),
    spell("Sabr", "Sabre", "caster", "Hit +40% & D +15%"),
    spell("Blnd", "Blind", "1 Enemy", "Dark status"),
    spell("Stop", "Stop", "All enemies", "Paralyse"),
    spell("Zap!", "Zap!","All enemies", "Time KO"),
    spell("XXXX", "XXXX","All enemies", "Death KO if <300 HP"),
    spell("Nuke", "Nuke", "All enemies", "Big damage")]


if __name__ == "__main__":
    #ListWhites.sort()
    #for i in ListWhites: print(i)
    ListBlacks.sort()
    for i in ListBlacks: print(i)