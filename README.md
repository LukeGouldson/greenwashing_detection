# Project Notes

## Project Summary

The project consists of two separate tasks: climate_relatedness_classification (a simple text classification task) and unsubstantiated_claims_classification (a more complex fact-checking task). The project involves the use of transformer models, primarily DistilRoBERTa (a compressed version of the RoBERTa architecture) and ClimateBERT (a domain-adapted version of DistilRoBERTa).

## Code Breakdown

### climate_relatedness_classification

Folder is split into three sections:

Data: contains datasets used for training
Fine_tuning: contains all code related to fine-tuned models
Vanilla: contains all code related to using models out-of-the-box

#### data

access_climateBUG.py is a python file which was used to download the climateBUG dataset from HuggingFace. It maintains the train/test split used by the developers

climateBUG folder contains the training and testing datasets as json files

#### fine_tuning

This folder contains:

* Two jupyter notebooks, one for fine-tuning distilroberta and one for fine-tuning climatebert. Both files have the same structure. For a breakdown of the code, see fine_tuning_cliamteBERT-base_climateBUG.ipynb, which has been commented for clarity

* A preprocessing.py python file, which handles the prepreprocessing of the climateBUG dataset and is imported from in the jupyter files

* A results folder, where all the eval_metric.json files are stored. In some cases, the full model has been saved too


#### vanilla

This folder contains:

* A jupyter notebook for running each model out-of-the-box

* A results folder where the eval_metrics.json files are stored

* A preprocessing.py python file, which contains the same code as the other preprocessing file, and was included here also for modularity

#### training_args.txt

This is a text file containing the training arguments used for each of the fine-tuning runs performed

### unsubstantiated_claims_classification

This folder is structured in exactly the same way as the climate_relatedness_classification. The key differences are:

* There is a second dataset, claimsKG, which was not used in the final project.

* There is a climate-fever-dataset-sample.jsonl file which was used for initial tests

### climateBERT_classification_test.ipynb

This is not a part of the final project, but was the first time I used a model from HuggingFace, so I opted to keep this in as evidence of progression
