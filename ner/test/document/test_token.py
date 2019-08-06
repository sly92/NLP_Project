import logging
import unittest
from ner.document import Token


LOGGER = logging.getLogger(__name__)


class test_token(unittest.TestCase):

    def setUp(self):
        self.object = Token(None,0,5,"mes test","alex test","le test marche")
    #Configurer les tests unitaires (si nécessaire)

    def test_text(self):
        self.assertEquals(self.object.text,"le test marche", "le test ne marche pas" )

    def test_pos(self):
        """Test le fonctionnement de la fonction 'Token.pos'."""
        self.assertEquals(self.object.pos,"mes test", "le test ne marche pas" )


    def test_shape(self):
        """Test le fonctionnement de la fonction 'Token.shape'."""
        self.assertEquals(self.object.shape,"alex test", "le test ne marche pas" )



if __name__ == '__main__':
    unittest.main()
