import spacy

def get_labels(file):
    print(file)
    data = open(file, "r", encoding='utf-8').readlines()

    data = [d for d in data if len(d.split("\t")) == 2]
    
    labels = [text.split("\t")[1].replace("\n", "") for text in data]
    labels = set(labels) 
    print(labels, '\n')
    return labels

get_labels("data/corpus_First_HAREM.txt")
get_labels("data/corpus_Paramopama.txt")
get_labels("data/corpus_paramopama+second_harem.txt")
get_labels("data/custom_eval.txt")
get_labels("data/custom_train.txt")