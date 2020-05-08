from classes import *
from Equips import weapon, listweapons, armor, listarmors, updateliste  # this works
from affichage import *
import os


clear = lambda: os.system('cls')

# Let's list the acronyms so both can be used.
Fi,Kn, BB, Ma, Th, Ni = Fighter, Knight, BlackBelt, Master, Thief, Ninja
RM, RW, WM, WW, BM, BW = RedMage, RedWizard, WhiteMage, WhiteWizard, BlackMage, BlackWizard
acrodicto = {"FI" : Fi, "KN" : Kn, "BB" : BB, "MA" : Ma, "TH" : Th, "NI" : Ni,
             "RM" : RM, "RW" : RW, "WM" : WM, "WW" : WW, "BM" : BM, "BW" : BW}






if __name__ == "__main__":
    clear()
    team = int(input("How many team members?"))
    print("Fi/Kn, BB/Ma, Th/Ni, RM/RW, WM/WW, BM/BW")

    #listchar = [char1, char2, char3, char4]
    listchar = []
    for _ in range(team):
        listchar.append(acrodicto[input("What is your 1st class? ").upper()]())

    listarmors = updateliste(listarmors, "Armory", listchar)
    listweapons = updateliste(listweapons, "Weapons", listchar)

    gaming = True
    while gaming :
        print("END = End the game, LA = List Armor, LW = List Weapons")
        command = input("What would you like to do? ").upper()
        clear()
        if command == "LA":
            print_table("Armory", listarmors, listchar)
        elif command == "LW":
            print_table("Weapons", listweapons, listchar)
        elif command == "END":
            print("Script Stopped")
            gaming = None