"""here we select a random sentence so we can write
    a new sentence in our file and redirect the conversation"""

import random
from .requete1 import *
from .requete2 import *

def dico_best_empty(entree, list_yes_no):
    """we select random sentence"""

    #choix_aleatoire = random.choice(3)
    #1 une anecdote
    choice_random = 1
    if choice_random == 1:
        answer = requete2()
        len_conteneur2 = len(answer) - 1
        randomm = random.randint(0, len_conteneur2)
        list_yes_no.append("phrase anecdocte "+str(randomm))
        return answer[randomm][0]


def yes_no(yes_no, entrance):
    """if the list contains anecdote sentence
    and that answer and yes we return a sentence"""

    cont = requete2()

    list_yes = ["oui"]
    list_no = ['non']

    conteneur_ans = cont[int(entrance[-1][-1])]
    print(conteneur_ans, "clinstiwoooooooooooooooooood")
    for i in list_yes:
        if yes_no == i:
            entrance.append("phrase schema")
            return conteneur_ans[2]

    for i in list_no:
        if yes_no == i:
            entrance.append("phrase schema")
            return conteneur_ans[1]
 
    return "*ronronne sois plus gentil*"
