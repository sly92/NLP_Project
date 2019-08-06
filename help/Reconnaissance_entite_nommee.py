# Run: python -m nltk.downloader words maxent_ne_chunker gutenberg maxent_treebank_pos_tagger averaged_perceptron_tagger
import nltk, re
from nltk.tokenize import sent_tokenize, word_tokenize

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() in ['ORGANIZATION','PERSON','GPE']:
            entity_names.append((' '.join([child[0] for child in t]),t.label()))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

# Input data
with open('C:/Users/bejaouis/Desktop/Ecole/5A/NLP/échantillons de texte/data/NER Sample.txt', 'r') as f:
    sample = f.read()

# Séparation des phrases
sentences = nltk.sent_tokenize(sample)

# Séparation des mots
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Étiquetage morpho-syntaxique
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

# Application de NER
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

entity_names = []
for tree in chunked_sentences:
    entity_names.extend(extract_entity_names(tree))

# Print unique entity names
print(set(entity_names))