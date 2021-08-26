from numpy.core.fromnumeric import transpose
from spacy.training import Corpus
import spacy

corpus = Corpus("spacy_data/corpus_First_HAREM.spacy")
nlp = spacy.blank("pt")
train_data = corpus(nlp)

for ex in train_data:
    print(ex.to_dict())
    break