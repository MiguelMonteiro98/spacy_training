import spacy

nlp = spacy.load('pt_core_news_md')


def get_labels(file):
    print(file)
    data = open(file, "r").readlines()

    data = [d for d in data if len(d.split("\t")) == 2]
    

    texts = [text.split("\t")[0] for text in data]
    labels = [text.split("\t")[1].replace("\n", "") for text in data]
    labels = set(labels) 
    print(labels, '\n')
    return labels

get_labels("data/corpus_First_HAREM.txt")
get_labels("data/corpus_Paramopama.txt")
get_labels("data/corpus_paramopama+second_harem.txt")