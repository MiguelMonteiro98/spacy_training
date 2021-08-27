import os
import sys

def run(model_name, gpu = False, train = False):

    if gpu:
        gpu_cmd = "--gpu-id 0"
    else:
        gpu_cmd = "--gpu-id -1"

    config_cmd = "python -m spacy init fill-config base_config.cfg config.cfg"
    spacy_path = "spacy_data/"

    
    dev_data = "custom_eval.spacy"
    train_data = "custom_train.spacy"

    data_path = spacy_path + train_data
    dev_path = spacy_path + dev_data

    train_path_changer = "--paths.train "+data_path

    dev_path_changer = "--paths.dev "+dev_path

    print("training data: " ,train_path_changer)
    print("evaluation data: " ,dev_path_changer)
    verbose = "--verbose"



    labels_cmd = "python -m spacy init labels config.cfg labels {} {} {} {}".format(verbose, train_path_changer, dev_path_changer, gpu_cmd)
    os.system(labels_cmd)

    train_cmd = "python -m spacy train config.cfg --output models/{} {} {} {}".format(model_name, train_path_changer, dev_path_changer, gpu_cmd)

    #train the thingy
    if train:
        os.system(train_cmd)

run("custom_training", gpu = False, train = True)