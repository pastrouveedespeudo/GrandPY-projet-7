"""here we are going to write the sentences that requete1 does not have
and we write in"""

def ecriture(entrance):
    """we opening requete1 source of our sentences"""
    liste = []

    file1 = open("fbapp/requete1.py", "r")

    liste.append(file1.read())

    liste[0] = liste[0][:-17]

    with open("fbapp/requete1.py", "w") as file:
        file.write((str(liste[0][:-2])\
                    + "\n"\
                    + "           [" + '"' +str(entrance) + '"]'\
                    +"," + "\n"\
                    + "           ]" + '\n'\
                    +"    "+"return liste"))
