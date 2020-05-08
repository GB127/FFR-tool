def print_table(what, liste, listechar):
    """Produces a string that represent the whole list along with
        the characteristics of the classes in the team. Then print it.
        Arguments:
            what (str) = "Armory" or "Weapons"
            liste (list) = uniform list of weapon or armor objects
            listechar = list of FFRclasses in the team
    """
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
