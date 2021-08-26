import os


config_cmd = "python -m spacy init fill-config base_config.cfg config.cfg"
spacy_path = "spacy_data/"
train_data = "corpus_First_HAREM.spacy"
dev_data = "corpus_paramopama+second_harem.spacy"

data_path = spacy_path + train_data
dev_path = spacy_path + dev_data

train_path_changer = "--paths.train "+data_path

dev_path_changer = "--paths.dev "+dev_path

print("training data: " ,train_path_changer)
print("evaluation data: " ,dev_path_changer)
verbose = "--verbose"



labels_cmd = "python -m spacy init labels config.cfg labels {} {} {}".format(verbose, train_path_changer, dev_path_changer)
os.system(labels_cmd)

train_cmd = "python -m spacy train config.cfg --output models {} {}".format(train_path_changer, dev_path_changer)

#train the thingy
os.system(train_cmd)