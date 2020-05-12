from spells import spell, ListWhites, ListBlacks, item, ListItems, ListKeyItems

def print_help():
    listofcommands = [
        "END = End the scrpt\n",

        "## = Use item/Weapon/armor",
        "KI = Key Items",
        "LA = List Armor",
        "LI = List Items",
        "LSB = List Spells Black",
        "LSW = List Spells White",
        "LT = List Team",
        "LW = List Weapons",
        "RK = Rank up"]
    string = "\n".join(listofcommands)
    print(string)


def print_items(command,listekeys):
    string = "-" * 27 + "\n"
    if command == "LI":
        string += "List of Items\n" + "-" * 27 + "\n"
        ListItems.sort()
        for ite in ListItems: 
            string += str(ite) + "\n"
        print(string)
    if command == "KI":
        string += "List of Key Items\n" + "-" * 27 + "\n"
        listekeys.sort()
        for no, ite in enumerate(listekeys):
            string += f'{str(no):<3}' + str(ite) + "\n"
        print(string)        


def print_table(listWA, listechar):
    """Produces a string that represent the whole list along with
        the characteristics of the classes in the team. Then print it.
        Arguments:
            liste (list) = uniform list of weapon or armor objects
            listechar = list of FFRclasses in the team
    """
    string = " " * 27 + "| X  | X  |"
    for char in listechar:
        string += f"{char.acro:^3}|"
    string += "\n" + ("-" * 38) + "----" * len(listechar)
    for no,i in enumerate(listWA):
        line = f'{str(no):<2}  ' + str(i)
        for char in listechar:
            line += f"{char.checkequip(i, True):^3}|"
        string += f"\n{line}"
    string += "\n" + ("-" * 38) + "----" * len(listechar)
    print(string)

def print_spells(command):
    if command == "LSW":
        ListWhites.sort()
        for sp in ListWhites : print(sp)
    if command == "LSB":
        ListBlacks.sort()
        for sp in ListBlacks : print(sp)


if __name__ == "__main__":
    print_help()