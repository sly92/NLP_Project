import logging
import unittest
import os

from data import DATA_DIR
from ner.document import Token, Document
from ner.document.Vectorizer import Vectorizer


LOGGER = logging.getLogger(__name__)


class test_vectorizer(unittest.TestCase):

    def setUp(self):
        self.object = Document()

    def test_encode_features(self):
        filename = os.path.join(DATA_DIR,"glove.6B.50d.txt")
        v = Vectorizer(filename)
        docs = []
        doc = self.object.create_from_text("This is a test. And this another.")
        docs.append(doc)
        doc = self.object.create_from_text("This is a test. And this another.")
        docs.append(doc)
        doc = self.object.create_from_text("This is a test. And this another.")
        docs.append(doc)

        words, pos, shapes = v.encode_features(docs)

        self.assertEquals(len(words), 6)


    def test_encode_annotation(self):
        filename = os.path.join(DATA_DIR,"glove.6B.50d.txt")
        v = Vectorizer(filename)
        documents = []
        doc = self.object.create_from_text("This is a test. And this another.")
        documents.append(doc)
        doc = self.object.create_from_text("This is a test. And this another.")
        documents.append(doc)
        doc = self.object.create_from_text("This is a test. And this another.")
        documents.append(doc)

        labels = v.encode_annotations(documents)

       # self.assertEquals(len(words), 6)
        print(labels)



if __name__ == '__main__':
    unittest.main()
