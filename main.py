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




def print_table(what, liste, listechar):
    string = " " * 27 + "| A  | E  |"
    for char in listechar:
        string += f"{char.acro:^3}|"
    string += "\n" + ("-" * 38) + "----" * len(listechar)
    for no,i in enumerate(liste):
        line = f'{str(no):<2}  ' + str(i)
        for char in listechar:
            line += f"{char.checkequip(what, i.cat, i.name, True):^3}|"
        string += f"\n{line}"
    string += "\n" + ("-" * 38) + "----" * len(listechar)
    print(string)


if __name__ == "__main__":
    clear()
    # team = input("How many characters in your team? [1,2,3,4]")
    team = int(input("How many team members? [1,2,3,4]"))
    print("Fi/Kn, BB/Ma, Th/Ni, RM/RW, WM/WW, BM/BW")
    listchar = []
    for _ in range(team):
        listchar.append(acrodicto[input("What is your 1st class? ").upper()]())

    #listchar = [char1, char2, char3, char4]
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