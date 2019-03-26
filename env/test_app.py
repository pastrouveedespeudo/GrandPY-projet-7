import fbapp.run as script


def test_no_ponctuation():
    parametre = "connais tu openclassrooms ?"
    sortie = "connais tu openclassrooms"

    assert script.no_ponctuation(parametre) == sortie


def test_search_dico():
    parametre = "voiture"
    sortie = "nf"
    
    assert script.search_dico(parametre) == sortie


def test_apostrohpe():
    parametre = "l'adresse"
    sortie = "l'adresse"

    assert script.apostrohpe(parametre) == sortie


def test_parsing_text():
    parametre = "salut"
    sortie = "salut"

    assert script.parsing_text(parametre) == sortie


def test_searching():
    parametre = "sa"
    sortie = 'Salzburg, 5020, Österreich', 47.8028273, 13.057954916199
    assert script.searching(parametre) == sortie

def test_searching2():
    parametre = "sdzaaaaaaaa"
    sortie = 'None'
    assert script.searching(parametre) == sortie


    
liste = []
answer = ["oui et toi ?"]
def test_dico_best_empty():
    parametre = "salut ca va ?", liste
    sortie = "oui et toi ?"


liste1 = ["oui"]
conteneur_ans = ["coucou"]
def test_yes_no():
    parametre = liste1, "oui"
    sortie = "coucou"
    




















































































