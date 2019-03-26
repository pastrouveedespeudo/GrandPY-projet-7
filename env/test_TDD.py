import fbapp.parsage as script
import unittest

class TTD(unittest.TestCase):

    def test_ponctuation(self):
        """Here we delete ponctuation"""
        
        #make a punctuation list
        self.assertEqual(script.no_ponctuation("bonjour ?"), "bonjour")
        #walk through each entrance element
        #compare the elements of the punctuation list with the entry
        #visulize last caractere is it " "? yes don't return it
        self.assertEqual(script.no_ponctuation(" "), " ")
        #remove punctuation

        self.assertEqual(script.no_ponctuation("bonjour ?"), "bonjour")
        


    def test_search_dico(self):
        """we surch word before " ' " it by e or a according to the noun"""
        #we search the substantive
        #we recover the div
        #from last step we searching nm or nf
        #we return it
        
        self.assertEqual(script.search_dico("l'ardoise"), "f")
        self.assertEqual(script.search_dico("l'antartique"), "nm")


    def test_apostrophe(self):
        """ we delete " ' " and replace it"""
        
        #we check the input sentence
        #we go through the list
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         "['connais', 'la', 'adresse', 'd'openclassrooms']")
        #indexing it
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         "[3]")
        #we search " ' " if we founding it we isolate it
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         '["d\'openclassrooms"]')
        #we delete it
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         "['d openclassrooms']")
        #transfom it like multiple element
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         "[['d', 'openclassrooms']]")       
        #if search_dico == nm : we replace ' by e
        #or a if search_dico == nf
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         ['de openclassrooms'])
        
        self.assertEqual(script.apostrohpe("connais la adresse d'openclassrooms"),
                         'de openclassrooms')

        #join it !
        self.assertEqual(script.apostrohpe("connais la adresse l'ardoise"),
                            
        #testing it without sentence                
        self.assertEqual(script.apostrohpe("l'ardoise"), "l'ardoise")


    def test_parsing_text(self):
        """If the catchphrase is we just take the last word"""

        #search match with catchpgrase
        #we take the last word into list
    
        self.assertEqual(script.parsing_text("Salut GrandPY  Est-ce que tu connais la adresse de Crest"),
                         "Crest")


    def test_searching(self):
        """Here we calling api geocode"""

        #we calling input data
        #we seaching address, latitude and longitude
        #we return it or return None
        
        self.assertEqual(script.searching("sa"),
                         ("Salzburg, 5020, Österreich", 47.8028273, 13.057954916199))

        
##if __name__ == "__main__":
##    pass




































