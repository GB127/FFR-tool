from FFclasses import *  # This imports all classes infos.
from Equips import weapon, listweapons, armor, listarmors, updateliste
from affichage import print_table, print_spells, print_items
from spells import KeyItem, ListKeyItems
import re
import os

clear = lambda: os.system('cls')

# Let's list the acronyms so both can be used if needed.
Fi,Kn, BB, Ma, Th, Ni = Fighter, Knight, BlackBelt, Master, Thief, Ninja
RM, RW, WM, WW, BM, BW = RedMage, RedWizard, WhiteMage, WhiteWizard, BlackMage, BlackWizard
acrodicto = {"FI" : Fi, "KN" : Kn, "BB" : BB, "MA" : Ma, "TH" : Th, "NI" : Ni,
             "RM" : RM, "RW" : RW, "WM" : WM, "WW" : WW, "BM" : BM, "BW" : BW}

def getitem(team, listtouse, which):
    itemused = listtouse[which]
    if isinstance(itemused, (weapon, armor)):
        team[int(input("Who?"))].equip(itemused)
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
    listarmors = updateliste(listarmors, listchar)
    listweapons = updateliste(listweapons, listchar)
    listofcommands = "\nEND = End the scrpt\n\nKI = Key Items\nLA = List Armor\nLI = List Items\nLSB = List Spells Black\nLSW = List Spells White\nLT = List Team\nLW = List Weapons\nRK = Rank up\n"
    print(listofcommands)

    gaming = True
    while gaming :
        command = input("What would you like to do? ").upper()
        print(type(command))
        clear()
        if command == "END":
            print("Script Stopped")
            gaming = None
        if command == "HELP":
            print(listofcommands)
        elif command == "LA":
            print_table(listarmors, listchar)
            currentlist = listarmors
        elif command == "LW":
            print_table(listweapons, listchar)
            currentlist = listweapons
        elif command == "LT":
            for i in listchar: print(i)
            currentlist = None
        elif command in ("LSW","LSB"):
            print_spells(command)
            currentlist = None
        elif command == "RK":
            for i, char in enumerate(listchar) : 
                listchar[i] = char.rankup()
            currentlist = None
        elif command in ("LI", "KI"):
            print_items(command, ListKeyItems)
            if command == "KI" : currentlist = ListKeyItems
        else:
            try: int(command)
            except ValueError:
                pass
            else: getitem(listchar, currentlist, int(command))




