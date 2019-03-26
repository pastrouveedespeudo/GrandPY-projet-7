"""Here we link between html, js pages and python processing"""
import os
import subprocess
from geopy.geocoders import Nominatim
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

import urllib.request
from PIL import Image
from flask import Flask
from flask import request
from flask import url_for
from flask import jsonify
from geopy.geocoders import Nominatim
import requests
import wikipediaapi
import random
import time
from .parsage import *
from .phrase_schema import *
from .phrase_anecdocte import *
from .convers import *
import os

LIST = []
LIST_SENTENCE = []
LIST_WIKI = []
LOCALISATION_WIKI = []
CONVERSATION = []


@app.route('/')
def home():
    """Here we just display home page"""
    return render_template("home.html")


@app.route('/tchat')
def tchat():
    """Here we just display home page"""
    return render_template("tchat.html")


@app.route('/effacer', methods=["GET", "POST"])
def effacer():
    eff = request.form['data']
    CONVERSATION = []


list_yes_no = ["phrase schema"]
@app.route('/answer', methods=["GET", "POST"]) 
def answer():
    """Here we request methods and we send into html page"""

    question = request.form['data']
    question1 = question.lower()
    sentence_schema = read_list(question1, list_yes_no)
    print(list_yes_no)
    sentence = '<div style="font-size:1.5vw; color:black;">'\
             + str(question)\
             + '<br>'\
             + str(sentence_schema)\
             + '</div>'
             
    CONVERSATION.append(sentence)

    return jsonify({'data':CONVERSATION})


@app.route('/img', methods=["GET", "POST"])
def img():

    img = request.form['data']

    liste = ['aurevoir.jpg', 'bonjourcava.jpg',
             'casentbizzardtontruk.jpg', 'cki.jpg',
             'cmonpoterico.jpg', 'connarquestion.jpg',
             'cquoicasemange.jpg', 'croooooooo.jpg',
             'croquetteebd.jpg', 'croquettequestion.jpg',
             'croquettttttte.jpg', 'evitequestion.jpg',
             'girencompris.jpg', 'griencapte.jpg', 'grosmot.jpg',
             'gstrictemenrriencdompris.jpg', 'heouiii.jpg',
             'iladitcroquette.jpg', 'imaginehinquoi.jpg',
             'injure.jpg', 'jaipascompris.jpg', 'moiaussicava.jpg',
             'nannn.jpg', 'nannnn.jpg', 'nannnnnnnnnnnnnnn.jpg',
             'nonrep.jpg', 'ohhctpasdumiel.jpg', 'one',
             'onestcopain.jpg', 'ontecoute.jpg', 'ontecoute2.jpg',
             'onvacasserlagueuleaqui.jpg', 'ouaisetquestion.jpg',
             'ouitjpire.jpg', 'pasdekeumhumhum.jpg',
             'posemoiuneadresse.jpg',
             'poussezvousjesuisinfirmier.jpg',
             'putinjaitropbouffer.jpg', 'questquya.jpg',
             'quette.jpg', 'quoi.jpg', 'quoiiii.jpg', 'quoitadisquoi.jpg',
             'tasunkeum.jpg', 'tasvrmntditcroquette.jpg',
             'taunecbsurtoi.jpg', 'taunemeuf.jpg',
             'tuveuxcasserlesgenouxaqui.jpg',
             'yauratoujourspire.jpg',
             'yvamedemanderuneadresseoui.jpg']

    a = random.choice(liste)
    return jsonify({'data':"<img src='static/convers/one/{}'\
                    style='width:100%;\
                    height:290px;'/>".format(a)})


@app.route('/geo', methods=["GET", "POST"])
def geo():
    """Here we send longitude data"""

    data_wiki = request.form['data']
    print(data_wiki)
    data_no_ponctuation = no_ponctuation(data_wiki)
    cleaning = apostrohpe(data_no_ponctuation)
    last_word = parsing_text(cleaning)
    search = searching(last_word)
    page = search[1]
    print(page)
    return jsonify({'data':page})


@app.route('/geo2', methods=["GET", "POST"])
def geo2():
    """Here we send latitude data"""

    data_wiki = request.form['data']
    data_no_ponctuation = no_ponctuation(data_wiki)
    cleaning = apostrohpe(data_no_ponctuation)
    last_word = parsing_text(cleaning)
    search = searching(last_word)
    page = search[2]
    print(page,'00000000000000000000000000000000')
    return jsonify({'data':page})


@app.route('/wiki', methods=["GET", "POST"])
def wiki():
    """He we send wikipedia stuff"""

    b = ""
    liste = [[], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [],
             [], [], []]
    c = 0
    data_wiki = request.form['data']
    print(data_wiki)
    if data_wiki == "":
        page = ""
        return jsonify({'data':page})
    else:
        data_no_ponctuation = no_ponctuation(data_wiki)
        cleaning = apostrohpe(data_no_ponctuation)
        last_word = parsing_text(cleaning)
        search = searching(last_word)
        if search == "None":
            page = "<div style='font-size:2vw; color:black;'>\
                   Rien trouvé désolé</div>"
            return jsonify({'data':page})
        else:
            addresse = []
            addresse.append(search[0])
            for i in addresse:
                for j in i:
                    liste[c].append(j)
                    if j == ',':
                        c += 1

    sentence_from_grandpy = ["Savez tu que :",
                             "T'avais-je dis que :",
                             "Une fois on m'a dit que :"]

    choice = random.choice(sentence_from_grandpy)

    element = "".join(liste[2][:-1])
    print(element,"0000000000000000000000elemennnnnnnnnnnnnnnnnnt")
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    page_py = wiki_wiki.page('{}'.format(element))
    existe = page_py.exists()
    if existe == True:
        page = ("<p style='color:black; font-size:2vw;'>\
                <strong>" + str(choice)\
                +"</strong>" + "<br>"\
                + str(page_py.sections[0:200]) + "...</p>")

        return jsonify({'data':page})

    else:
        page = "<p style='color:black; font-size:2vw;'>\
                Oups je n'ai rien trouvé</p>"
        return jsonify({'data':page})


@app.route('/data', methods=["GET", "POST"])
def data():
    """Here, we just recup data with request form"""
    """from jquerry function() who define content from input"""

    data = request.form['data']
    data_no_ponctuation = no_ponctuation(data)
    cleanning = apostrohpe(data_no_ponctuation)

    last_word = parsing_text(cleanning)

    date = time.strftime("%A %d %B %Y %H:%M:%S")
    date = str(date)

    LIST.append("<div style='font-style:italic;font-size:2vw;\
                color:black;'>A {}</div>".format(date))

    LIST.append("<div style='color:black; font-size:2vw;'>\
                <strong>Votre question: </strong></div>")

    LIST.append("<div style='font-style:italic;\
                font-size:2.3vw; color:black;'>{}</div>".format(data))


    if data:
        var = searching(last_word)
        if var == "None":
            LIST.append("<div style='font-style:italic;\
                        font-size:2vw;color:black;'>\
                        <strong>Chat alors pas une addresse trouvée: \
                        </strong></div>")
            
            return jsonify({'data':LIST})
        
        else:
            LIST.append("<div style='font-style:italic;\
                        font-size:2.5vw;color:black;'>\
                        <strong>Chat alors une addresse trouvée: \
                        </strong></div>")

            LIST.append("<div style='font-size:2.5vw;\
                        color:black;'>\
                        <strong>{}</strong>\
                        </div>".format(var))

            LIST.append("<br>")

            return jsonify({'data':LIST})

    return jsonify({'error':'...'})


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
