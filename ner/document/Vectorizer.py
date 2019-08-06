import gensim
from typing import List

from ner.document import Document


class Vectorizer:
    """ Transform a string into a vector representation"""

    def __init__(self, word_embedding_path: str):
        """
        :param word_embedding_path: path to gensim embedding file
        """
        # TODO: Load word embeddings from file

        # Load embeddings
        self.word_embeddings = gensim.models.KeyedVectors.load_word2vec_format(word_embedding_path, binary=False)

        # Create POS to index dictionary
        self.pos2index = {'PAD': 0, 'TO': 1, 'VBN': 2, "''": 3, 'WP': 4, 'UH': 5, 'VBG': 6, 'JJ': 7, 'VBZ': 8, '--': 9,
                          'VBP': 10, 'NN': 11, 'DT': 12, 'PRP': 13, ':': 14, 'WP$': 15, 'NNPS': 16, 'PRP$': 17,
                          'WDT': 18, '(': 19, ')': 20, '.': 21, ',': 22, '``': 23, '$': 24, 'RB': 25, 'RBR': 26,
                          'RBS': 27, 'VBD': 28, 'IN': 29, 'FW': 30, 'RP': 31, 'JJR': 32, 'JJS': 33, 'PDT': 34, 'MD': 35,
                          'VB': 36, 'WRB': 37, 'NNP': 38, 'EX': 39, 'NNS': 40, 'SYM': 41, 'CC': 42, 'CD': 43, 'POS': 44,
                          'LS': 45}

        # TODO: Create shape to index dictionary
        self.shape2index = {'NL': 0, 'NUMBER': 1, 'SPECIAL': 2, 'ALL-CAPS': 3, '1ST-CAP': 4, 'LOWER': 5, 'MISC': 6 }

        # TODO: Create labels to index dictionary
        self.labels2index = {'O': 0,
                                'PER': 1, 'I-PER':2, 'B-PER': 3,
                                'LOC': 4, 'I-LOC': 5, 'B-LOC': 6,
                                 'ORG': 7, 'I-ORG': 8, 'B-ORG': 9,
                                'MISC': 10, 'I-MISC': 11, 'B-MISC': 12}

    def encode_features(self, documents: List[Document]):
        """
        Creates a feature matrix for all documents in the sample list
        :param documents: list of all samples as document objects
        :return: lists of numpy arrays for word, pos and shape features.
                 Each item in the list is a sentence, i.e. a list of indices (one per token)
        """

        words, pos, shapes = [], [], []

        # TODO:
        # Loop over documents
        for doc in documents:
        #    Loop over sentences
            for sentence in doc.sentences:
                words_tmp, pos_tmp, shapes_tmp = [], [], []
        #        Loop over tokens
                for token in sentence.tokens:
        #           Convert features to indices
                    pos_tmp.append(self.pos2index[token.pos])
                    shapes_tmp.append(self.shape2index[token.shape])

                    if(token.text.lower() in self.word_embeddings.index2word):
                        words_tmp.append(self.word_embeddings.index2word.index(token.text.lower()))
                    else:
                        words_tmp.append(0)

                pos.append(pos_tmp)
                words.append(words_tmp)
                shapes_tmp.append(shapes_tmp)

        return words, pos, shapes


    def encode_annotations(self, documents:List[Document]):
        """
        Creates the Y matrix representing the annotations (or true positives) of a list of documents
        :param documents: list of documents to be converted in annotations vector
        :return: numpy array. Each item in the list is a sentence, i.e. a list of labels (one per token)
        """

        # Loop over documents
        labels = []
        for doc in documents:
            #    Loop over sentences
            label_index =[]
            for sentence in doc.sentences:
                #Loop over tokens
                for token in sentence.tokens:
                #convert label to numerical representation
                   label_index.append(self.labels2index[token.label])

                labels.append(label_index)

        return labels

