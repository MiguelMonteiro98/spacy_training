import os

data_dir = "data/"
prep_dir = "prep_data/"

def prep_data(file):
    print("Preparing ", file)
    data_list = open(data_dir + file, encoding='utf-8').readlines()
    result = []

    tags = {
        "ORGANIZACAO\n" : "ORG\n",
        "LOCAL\n" : "LOC\n",
        "PESSOA\n" : "PER\n",

    }

    for idx, data in enumerate(data_list):
        if data != "\n":
            text, tag = data.split("\t")
            tag = tags.get(tag, tag)

            #B and I tags??
            if tag != 'O\n':
                if idx > 0 and result[idx - 1] != '\n' and tag in result[idx - 1].split(" ")[1]:
                    tag = 'I-'+tag
                else:
                    tag = 'B-'+tag
            data = text + ' ' + tag
        result.append(data)


    with open(prep_dir + file, "w", encoding='utf-8') as fp:
        fp.writelines(result)

    os.system("python -m spacy convert "+prep_dir + file+" spacy_data/ -c ner -n 10")

prep_data("corpus_First_HAREM.txt")
prep_data("corpus_Paramopama.txt")
prep_data("corpus_paramopama+second_harem.txt")
prep_data("custom_eval.txt")
prep_data("custom_train.txt")