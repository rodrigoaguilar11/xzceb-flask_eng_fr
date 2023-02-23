import sys        
sys.path.append('/home/project/xzceb-flask_eng_fr/final_project/machinetranslation')       
 
import unittest
from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertEqual(english_to_french("Thanks"), "Merci") 
        self.assertNotEqual(english_to_french("Hello"), "Banana") 
        

class TestDouble(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Merci"), "Thank you")
        self.assertNotEqual(french_to_english("Bonjour"), "Banana")
        
unittest.main()