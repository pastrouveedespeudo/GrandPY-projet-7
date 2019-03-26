"""Here we decide of the sentence to put according to the answer"""
from .ecriture import *
from .requete1 import *
from .requete2 import *
from .phrase_anecdocte import *

def read_list(entrance, list_yes_no):
    """here we choose to put a logical continuation\
    sentence of an existing conversation or we put\
    an anecdotal sentence so that we can refocus\
    the discussion and be able to collect\
    the non-existing sentence"""
    liste = requete1()
    sentence_after = []
    if list_yes_no[-1] == "phrase schema":
        count = 0
        for i in liste:
            count1 = 0
            for j in liste[count]:
                if entrance == j:
                    try:
                        sentence_after.append(liste[count][count1 + 1])
                        dico_best = sorting_list(sentence_after)
                        list_yes_no.append("phrase schema")
                    except:
                        dico_best = "*ronronne repond le savais tu ? :3*"
                    return dico_best
                elif entrance != j:
                    list_yes_no.append("phrase anecdocte")
                count1 += 1
            count += 1

    if list_yes_no[-1][:-2] == "phrase anecdocte":
        dico_best = yes_no(entrance, list_yes_no)
        return dico_best
    elif list_yes_no[-1] == "phrase anecdocte":
        list_yes_no.append("phrase anecdocte")
        dico_best = dico_best_empty(entrance, list_yes_no)
        return dico_best
    
    return "*ronronne repond le savais tu ? :3*"


def sorting_list(entrance):
    """Here we go see all matches from entrance"""

    liste = []
    for i in entrance:
        liste.append(i)
    for i in liste:
        i = i.split()

    dico = {}
    count = 0
    for i in liste:
        dico[i] = -1

    for i in liste:
        for key, values in dico.items():
            if i == key:
                dico[i] += 1

    dico_best = max(dico)

    return dico_best
