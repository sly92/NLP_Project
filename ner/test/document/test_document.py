import logging
import unittest
from ner.document import Document
from ner.document import Sentence


LOGGER = logging.getLogger(__name__)


class test_token(unittest.TestCase):

    def setUp(self):
        self.object = Document()

    #Configurer les tests unitaires (si nécessaire)
    def test_create_from_text(self):
        doc = self.object.create_from_text("This is a test. And this another.")
        self.assertEquals(len(doc.tokens), 9, '')
        self.assertEquals(len(doc.sentences), 2, '')


if __name__ == '__main__':
    unittest.main()
