from classes import FFRclasses,\
    Fighter, Knight,\
    Thief, Ninja,\
    BlackBelt, Master,\
    RedMage, RedWizard,\
    WhiteMage, WhiteWizard,\
    BlackMage, BlackWizard
import os
clear = lambda: os.system('cls')
clear()

# Let's list the acronyms so both can be used.
Fi,Kn, BB, Ma, Th, Ni = Fighter, Knight, BlackBelt, Master, Thief, Ninja
RM, RW, WM, WW, BM, BW = RedMage, RedWizard, WhiteMage, WhiteWizard, BlackMage, BlackWizard
acrodicto = {"FI" : Fi, "KN" : Kn, "BB" : BB, "MA" : Ma, "TH" : Th, "NI" : Ni,
             "RM" : RM, "RW" : RW, "WM" : WM, "WW" : WW, "BM" : BM, "BW" : BW}





if __name__ == "__main__":
    clear()  # Note that this removes the ability to check if ran on the correct place
    print("Fi/Kn, BB/Ma, Th/Nin, RM/RW, WM/WW, BM/BW")
    char1 = acrodicto[input("What is your 1st class? ").upper()]()
    char2 = acrodicto[input("What is your 2nd class? ").upper()]()
    char3 = acrodicto[input("What is your 3rd class? ").upper()]()
    char4 = acrodicto[input("What is your 4th class? ").upper()]()


