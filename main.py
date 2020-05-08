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
    print(" " * 27 + "| A  | E  |" + f"{char1.acro:^3}|{char2.acro:^3}|{char3.acro:^3}|{char4.acro:^3}|")
    print("-" * 53)
    for no,i in enumerate(liste):
        line = f'{str(no):<2}  ' + str(i) + f"{char1.checkequip(what, i.cat, i.name, True):^3}|"  + f"{char2.checkequip(what, i.cat, i.name, True):^3}|"  + f"{char3.checkequip(what, i.cat, i.name, True):^3}|"  + f"{char4.checkequip(what, i.cat, i.name, True):^3}|"
        print(line)
    print("-" * 53)





if __name__ == "__main__":
    clear()  # Note that this removes the ability to check if ran on the correct place
    print("Fi/Kn, BB/Ma, Th/Ni, RM/RW, WM/WW, BM/BW")
    
    char1 = acrodicto[input("What is your 1st class? ").upper()]()
    char2 = acrodicto[input("What is your 2nd class? ").upper()]()
    char3 = acrodicto[input("What is your 3rd class? ").upper()]()
    char4 = acrodicto[input("What is your 4th class? ").upper()]()
    

    # char1, char2, char3, char4 = BB(), BM(), Th(), BM()
    listchar = [char1, char2, char3, char4]
    listarmors = updateliste(listarmors, "Armory", listchar)
    listweapons = updateliste(listweapons, "Weapons", listchar)

    gaming = True
    while gaming :
        print("END = End the game, LA = List Armor, LW = List Weapons")
        command = input("What would you like to do? ").upper()
        clear()
        if command == "LA":
            print_table("Armory", listarmors, listchar)
            print("A = Absorb      E = Evasion")
            print("-" * 53)
        elif command == "LW":
            print_table("Weapons", listweapons, listchar)
            print("D = Damage      H = Hit %")
            print("-" * 53)
        elif command == "END":
            print("Script Stopped")
            gaming = None