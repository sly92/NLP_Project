#import nltk
#nltk.help.upenn_tagset()
import os

from ner.document import Document
from ner.document.Interval import Interval


class Parser(object):
    """Classe parente pour tous les parsers"""
    def create(self):
        return self

    def read(self, content: str) -> Document:
            """Reads the content of a NER/POS data file and returns one document instance per document it finds."""
            enp =  EnglishNerParser()
            enp.read(content)

    def read_file(self, filename: str) -> Document:
        with open(filename, 'r', encoding='utf-8') as fp:
            content = fp.read()
        return self.read(content)

class SimpleTextParser(Parser):
    def read(self, content: str) -> Document:
        return Document().create_from_text(content)

class EnglishNerParser(Parser):
    def read(self, content: str) -> Document:
            """Reads the content of a NER/POS data file and returns one document instance per document it finds."""
            # 1. Split the text in documents using string '-DOCSTART- -X- O O' and loop over it
            # 2. Split lines and loop over
            # 3. Make vectors of tokens and labels (colunn 4) and at the '\n\n' make a sentence
            # 4. Create a Document object

            documents = []
            documents_readed = []
            sentences_readed = []
            sentences = []
            tokens = []
            words = []
            labels = []

            documents_readed = content.split('-DOCSTART- -X- O O')

            #print(documents)

            for document in documents_readed:
                if (document == ""):
                    continue
                start=0
                sentences_readed = document.split("\n\n")
                for sentence in sentences_readed:
                    lines = sentence.split("\n")
                    if (len(lines) > 1):
                        for line in lines:
                            tokens = line.split(' ')
                            words.append(tokens[0])
                            labels.append(tokens[3])
                    else:
                        continue
                    sentences.append(Interval(start,start + len(sentence)))
                    start += len(sentence)+1

                doc = Document().create_from_vectors(words, sentences, labels)
                documents.append(doc)

            return documents

def main():
    p = Parser()
    doc = p.read_file("./data/eng.testa.txt")
    print(doc)
   # enp.read(content)

if __name__ == "__main__":
    main()