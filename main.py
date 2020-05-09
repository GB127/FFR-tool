from FFclasses import *
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
    print("Fi, BB, Th, RM, WM, BM")

    #listchar = [BB(), Kn(), Fi(), RM()]
    listchar = []
    for _ in range(team):
        listchar.append(acrodicto[input("What is the class? ").upper()]())
    for i in listchar : print(i)

    listarmors = updateliste(listarmors, listchar)
    listweapons = updateliste(listweapons, listchar)

    gaming = True
    while gaming :
        print("END = End the game, LA = List Armor, LW = List Weapons, LT = List Team, RK = Rank up")
        command = input("What would you like to do? ").upper()
        clear()
        if command == "LA":
            print_table(listarmors, listchar)
        elif command == "LW":
            print_table(listweapons, listchar)
        elif command == "LT":
            for i in listchar: print(i)
        elif command == "RK":
            for i, char in enumerate(listchar) : 
                listchar[i] = char.rankup()
        elif command == "END":
            print("Script Stopped")
            gaming = None