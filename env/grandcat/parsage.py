"""This is methods to check the answers"""

import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


def no_ponctuation(entrance):
    """here we searching punctuation, and we erase it"""

    new = [i for i in entrance if i != "?" and i != "!" and i != "."]

    try:
        if new[-1] == " ":
            return "".join(new[:-1])
        else:
            return "".join(new)
    except:
        pass
        #new empty user click into enter without input ?

    return "".join(new)


def search_dico(data):
    """Here we search substantive of the next word"""

    path = "http://www.cnrtl.fr/definition/{}/substantif"
    path = path.format(data)
    
    request = requests.get(path)
    page = request.content
    soup = BeautifulSoup(page, "html.parser")
    propertyy = soup.find_all("div")

    fem = str(propertyy).find("fém")
    masc = str(propertyy).find("masc")

    if fem >= 0:
        return "nf"
    elif masc >= 0:
        return "nm"
    else:
        return "nm"


def apostrohpe(data):
    """Here we deleting apostrophe and add e or a from search_dico"""


    splite = data.split()
    b = [i for i in splite[-1] if i == "'"]

    if b != []:
        
        splite = data.split()
        indexing = [splite.index(i) for i in splite for j in i if j == "'"]
        take_apostophe = [i for i in splite for j in i if j == "'"]
        replacing = [i.replace("'", " ") for i in take_apostophe]
        splite2 = [i.split() for i in replacing]
        apo_to_a_e = [str(i[0]) + "a" + " " + str(i[1]) if search_dico(i[1]) == "nf" else str(i[0]) + "e" +  " " + str(i[1])
              for i in splite2]
        apo_to_a_e = " ".join(apo_to_a_e)

        return apo_to_a_e   

    else:
        return data



def parsing_text(data):
    """Here we'll go to parsing data \
    if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de\
    we juste take the last word from the sentence"""

    separate_element = data.split()
    list_into_list = [i.split() for i in separate_element]
    join_list = [",".join(j) for i in list_into_list for j in i]
    unification = str(join_list[-1]).replace(",","")

    return unification


def searching(parameter):
    """Here we searching from Python modul(geopy.geocoders)\
    address from the input from html page"""

    geocoder = Nominatim(user_agent="run.py")
    #parametre is data recup from data()
    try:
        location = geocoder.geocode(parameter, True, 30)
        localisation = location.address
        localisation = str(localisation)

        #define data from geopy.geocoders into var
        address = location.address
        latitude = location.latitude
        longitude = location.longitude
        return address, latitude, longitude
    except:
        return "None"
