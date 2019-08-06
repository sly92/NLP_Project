import logging
import unittest
from ner.document import Interval


LOGGER = logging.getLogger(__name__)


class test_token(unittest.TestCase):

    def setUp(self):
        self.object = Interval(0,5)
        self.object2 = Interval(0,5)


    #Configurer les tests unitaires (si nécessaire)

    def test__len__(self):
        self.assertEquals(self.object.__len__(),5, "le test ne marche pas !!!" )

    def test_overlaps(self):
        self.assertTrue(self.object.overlaps(self.object2))


if __name__ == '__main__':
    unittest.main()
