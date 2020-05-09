from FFclasses import *
from Equips import weapon, listweapons, armor, listarmors, updateliste  # this works
from affichage import print_table, print_spells
import os


clear = lambda: os.system('cls')

# Let's list the acronyms so both can be used.
Fi,Kn, BB, Ma, Th, Ni = Fighter, Knight, BlackBelt, Master, Thief, Ninja
RM, RW, WM, WW, BM, BW = RedMage, RedWizard, WhiteMage, WhiteWizard, BlackMage, BlackWizard
acrodicto = {"FI" : Fi, "KN" : Kn, "BB" : BB, "MA" : Ma, "TH" : Th, "NI" : Ni,
             "RM" : RM, "RW" : RW, "WM" : WM, "WW" : WW, "BM" : BM, "BW" : BW}



if __name__ == "__main__":
    clear()
    team = int(input("How many team members? "))
    print("Fi, BB, Th, RM, WM, BM")

    #listchar = [BB(), Kn(), Fi(), RM()]
    listchar = []
    for _ in range(team):
        listchar.append(acrodicto[input("What is the class? ").upper()]())

    listarmors = updateliste(listarmors, listchar)
    listweapons = updateliste(listweapons, listchar)
    listofcommands = "\nEND = End the scrpt\n\nLA = List Armor\nLSB = List Spells Black\nLSW = List Spells White\nLT = List Team\nLW = List Weapons\nRK = Rank up\n"



    gaming = True
    while gaming :
        print(listofcommands)
        command = input("What would you like to do? ").upper()
        print(type(command))
        clear()
        if command == "LA":
            print_table(listarmors, listchar)
        elif command == "LW":
            print_table(listweapons, listchar)
        elif command == "LT":
            for i in listchar: print(i)
        elif command in ("LSW","LSB"):
            print_spells(command)
        elif command == "RK":
            for i, char in enumerate(listchar) : 
                listchar[i] = char.rankup()
        elif command == "END":
            print("Script Stopped")
            gaming = None