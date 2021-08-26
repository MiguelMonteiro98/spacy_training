# spacy_training

## **Directories**

### data

 - Contains raw NER labelled datasets
   - First harem
   - Paramopama
   - Paramopama + second harem
 - All datasets contain the labels: 'O', 'ORGANIZACAO', 'LOCAL', 'PESSOA', 'TEMPO'.
 - The first harem data set also contains the 'VALOR' label.

 ### prep_data

 - Contains prepared datasets to be recognized by spacy convert command

 ### spacy_data

 - Contains data that will be fed to models, generated .spacy files by spacy convert

 ### displacy

 - Some displacy generated files by evaluate commands

 ### labels

 - Label documents for training generated by init labels in training.py

 ### metrics

 - Json files of metrics given by spacy evaluate commands

 ### models

 - trained models
   - **harem1_par**
     - training set: harem 1
     - evaluation set: paramonpana + second harem
     - 
   - **par_harem1**
     - training set: paramonpana + second harem
     - evaluation set: harem 1
   - **harem1**
     - training set: harem 1
     - evaluation set: harem 1
   - **pa_harem2**
     - training set: paramonpana + second harem
     - evaluation set: paramonpana + second harem

## **Evaluation**

Each model was evaluated with both harem1 and Paramopama + second harem.

Ideally, I would like to test it with an external data set, but for now this is it.

While the overall f-score is relevant, it is important to check the f-score for each label, since the presence/absence of the labels 'VALOR' lowers the global f-score.

I also present a baseline for the 'LOC', 'ORG' and 'PER' labels available in the 'pt_core_news_md' dataset.

Precision and recall metrics are available in the metrics folder or on the **evaluate_nb.ipynb** , under each model file. Table only shows f-score for simplicity.

| Model      | Eval dataset | Global f-s | LOC f-s | ORG f-s | TEMPO f-s | PER f-s | VALOR f-s |
|------------|---------|:----------:|:-------:|:-------:|:---------:|:-------:|:---------:|
| baseline   | harem1  |    0.397   |  0.575  |  0.325  |     0     |  0.550  |     0     |
| harem1_par | harem1* |    0.871   |  0.886  |  0.827  |   0.783   |  0.939  |   0.832   |
| harem1_par | par_h2  |    0.642   |  0.764  |  0.521  |   0.576   |  0.652  |     0     |
| par_harem1 | harem1  |    0.569   |  0.705  |  0.535  |   0.473   |  0.603  |     0     |
| par_harem1 | par_h2* |    0.856   |  0.894  |  0.756  |   0.820   |  0.887  |     0     |
| harem1     | harem1* |    0.981   |  0.982  |  0.974  |   0.978   |  0.990  |   0.980   |
| harem1     | par_h2  |    0.600   |  0.720  |  0.478  |   0.605   |  0.619  |     0     |
| pa_harem2  | harem1  |    0.550   |  0.667  |  0.550  |   0.434   |  0.595  |     0     |
| pa_harem2  | par_h2* |    0.955   |  0.963  |  0.915  |   0.952   |  0.972  |     0     |

\* - model trained on the same dataset of the evaluation

Unsurprisingly, the models perform better on the datasets they were trained on.

But the pairs of models harem1_par/harem1 and par_harem1/pa_harem2 don't show significant differences
when evaluated on the dataset they were not trained on. There is a slight advantage for the model with a different eval set from the training set, but I wouldn't call it significant.

This is possibly due to the impact of the 'VALOR' class in the training/evaluation.

## **Next steps/ideas**
 - Some weird entities are showing up, check displacy htmls to try to figure out what's going on.
 - Try to find another dataset with the same labels and train (to get rid of the possible 'VALOR' impact)
   - So far, unsucessful
 - Split the pa_harem2 dataset in two - since it is quite large - and try to train with the split set as train/eval and check results on eval set?
 - Hyperparameters?
