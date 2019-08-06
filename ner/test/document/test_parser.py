import logging
import os
import unittest
from ner.document import Document
from ner.document.Parser import EnglishNerParser
from ner.test.document.data import DATA_DIR


LOGGER = logging.getLogger(__name__)


class test_parser(unittest.TestCase):

    #Configurer les tests unitaires (si nécessaire)
    def test_EnglishNerParser(self):
        doc = EnglishNerParser().read_file(os.path.join(DATA_DIR), 'ner', 'eng.testa.txt')
        self.assertEquals(len(doc), 216, 'Some documents were extracted')


if __name__ == '__main__':
    unittest.main()
