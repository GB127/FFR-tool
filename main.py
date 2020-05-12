from FFclasses import *  # This imports all classes infos.
from Equips import weapon, listweapons, armor, listarmors, updateliste
from affichage import print_table, print_spells, print_items, print_help
from spells import KeyItem, ListKeyItems
import os

clear = lambda: os.system('cls')

# Let's list the acronyms so both can be used if needed.
Fi,Kn, BB, Ma, Th, Ni = Fighter, Knight, BlackBelt, Master, Thief, Ninja
RM, RW, WM, WW, BM, BW = RedMage, RedWizard, WhiteMage, WhiteWizard, BlackMage, BlackWizard
acrodicto = {"FI" : Fi, "KN" : Kn, "BB" : BB, "MA" : Ma, "TH" : Th, "NI" : Ni,
             "RM" : RM, "RW" : RW, "WM" : WM, "WW" : WW, "BM" : BM, "BW" : BW}

def getitem(team, listtouse, which):
    try:
        itemused = listtouse[which]
    except IndexError:
        print("Number entereed not in list")
        return
    else:
        if isinstance(itemused, (weapon, armor)):
            print("Weapon/Armor to be equiped:")
            print(itemused)
            print("\nTeam")
            for no,i in enumerate(team) : print(no, " ", i.__class__.__name__)
            team[int(input("Who? [#]"))].equip(itemused)
        elif isinstance(itemused, KeyItem):
            itemused.founduse()

if __name__ == "__main__":
    clear()
    team = int(input("How many team members? "))
    print("Fi, BB, Th, RM, WM, BM")

    # listchar = [BB(), Fi(), RM()]
    listchar = []
    for _ in range(team):
        listchar.append(acrodicto[input("What is the class? ").upper()]())

    currentlist = None
    listarmors2 = updateliste(listarmors, listchar)
    listweapons2 = updateliste(listweapons, listchar)

    print_help()


    gaming = True
    while gaming :
        command = input("What would you like to do? ").upper()
        clear()
        if command == "END":
            print("Script Stopped")
            gaming = None
        if command == "HELP":
            print_help()
        elif command == "LA":
            print_table(listarmors2, listchar)
            currentlist = listarmors2
        elif command == "LW":
            print_table(listweapons2, listchar)
            currentlist = listweapons2
        elif command == "LT":
            for i in listchar: print(i)
            currentlist = None
        elif command in ("LSW","LSB"):
            print_spells(command)
            currentlist = None
        elif command == "RK":
            for i, char in enumerate(listchar) : 
                listchar[i] = char.rankup()
            listarmors2 = updateliste(listarmors, listchar)
            listweapons2 = updateliste(listweapons, listchar)
            currentlist = None
        elif command in ("LI", "KI"):
            print_items(command, ListKeyItems)
            if command == "KI" : currentlist = ListKeyItems
        else:
            try: int(command)
            except ValueError:
                pass
            else:
                getitem(listchar, currentlist, int(command))
                listarmors = updateliste(listarmors, listchar)
                listweapons = updateliste(listweapons, listchar)





