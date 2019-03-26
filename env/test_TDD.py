import fbapp.parsage as script
import unittest

class TTD(unittest.TestCase):

    def test_ponctuation(self):
        """Here we delete ponctuation"""
        
        #make a punctuation list
        #walk through each entrance element
        #compare the elements of the punctuation list with the entry
        #remove punctuation

        self.assertEqual(script.no_ponctuation("bonjour ?"), "bonjour")
        
    def test_hello(self):
        self.assertEqual(script.hello_world(), 'hello world')        


    def test_search_dico(self):
        """we surch word before " ' " it by e or a according to the noun"""
        #we search the substantive
        #we recover the div
        #from last step we searching nm or nf
        #we return it
        
        self.assertEqual(script.search_dico("l'ardoise"), "nm")


    def test_apostrophe(self):
        """ we delete " ' " and replace it"""
        
        #we check the input sentence
        #we go through the list
        #we search " ' "
        #if search_dico == nm : we replace ' by e
        #or a if search_dico == nf
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




































