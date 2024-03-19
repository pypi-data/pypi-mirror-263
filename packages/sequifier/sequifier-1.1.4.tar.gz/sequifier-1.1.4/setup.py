# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sequifier', 'sequifier.config']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23,<2.0',
 'onnx>=1.15.0,<2.0.0',
 'onnxruntime>=1.17,<2.0',
 'pandas>=2.0,<3.0',
 'poetry>=1.3,<2.0',
 'pydantic>=1.10,<2.0',
 'pytest>=7.2,<8.0',
 'pyyaml>=6.0,<7.0',
 'torch>=2.0,<3.0']

entry_points = \
{'console_scripts': ['sequifier = sequifier.sequifier:main']}

setup_kwargs = {
    'name': 'sequifier',
    'version': '1.1.4',
    'description': 'Train a transformer model with the command line',
    'long_description': '<img src="./design/sequifier.png">\n\n\n### one-to-one and many-to-one autoregression made easy\n\nSequifier enables sequence classification or regression for time based sequences using transformer models, via CLI.\nThe specific configuration of preprocessing, which takes a single or multi-variable columnar data file and creates\ntraining, validation and test sequences, training, which trains a transformer model, and inference, which calculates\nmodel outputs for data (usually the test data from preprocessing), is done via configuration yaml files.\n\n\\\n\\\n\\\n## Overview\nThe sequifier package enables:\n  - the extraction of sequences for training\n  - the configuration and training of a transformer classification model\n  - inference on data with a trained model\n\n\n## Other materials \nIf you want to first get a more specific understanding of the transformer architecture, have a look at\nthe [Wikipedia article.](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))\n\nIf you want to see a benchmark on a small synthetic dataset with 10k cases, agains a random forest,\nan xgboost model and a logistic regression, check out [this notebook.](./documentation/demos/benchmark-small-data.ipynb)\n\n\n## Complete example how to build and apply a transformer sequence classifier with sequifier\n\n1. create a conda environment with python >=3.9 activate and run\n```console\npip install sequifier\n```\n2. create a new project folder (at a path referred to as `PROJECT PATH` later) and a `configs` subfolder\n3. copy default configs from repository for preprocessing, training and inference\n4. adapt preprocess config to take the path to the data you want to preprocess and set `project_path` to`PROJECT PATH`\n5. run \n```console\nsequifier --preprocess --config_path=[PROJECT PATH]/configs/preprocess.yaml\n```\n6. the preprocessing step outputs a "data driven config" at `[PROJECT PATH]/configs/ddconfigs/[FILE NAME]`. It contains the number of classes found in the data, a map of classes to indices and the oaths to train, validation and test splits of data. Adapt the `dd_config` parameter in `train-on-preprocessed.yaml` and `infer.yaml` in to the path `[PROJECT PATH]/configs/ddconfigs/[FILE NAME]`and set `project_path` to `PROJECT PATH` in both configs\n7. run\n```console\nsequifier --train --on-preprocessed --config_path=[PROJECT PATH]/configs/train-on-preprocessed.yaml\n```\n8. adapt `inference_data_path` in `infer.yaml`\n9. run\n```console\nsequifier --infer --config_path=[PROJECT PATH]/configs/infer.yaml\n```\n10. find your predictions at `[PROJECT PATH]/outputs/predictions/sequifier-default-best_predictions.csv`\n\n\n## More detailed explanations of the three steps\n#### Preprocessing of data into sequences for training\n\nThe preprocessing step is designed for scenarios where for timeseries or timeseries-like data,\nthe prediction of the next data point of a particular variable from prior values of that variable\nand (optionally) other variables is of interest.\nIn cases of sequences where only the last item is a valid target, the preprocessing\nstep should not be executed.\n\nThis step presupposes input data with three columns: "sequenceId" and "itemPosition", and a column\nwith the variable that is the prediction target.\n"sequenceId" separates different sequences and the itemPosition column\nprovides values that enable sequential sorting. Often this will simply be a timestamp.\nYou can find an example of the preprocessing input data at [documentation/example_inputs/preprocessing_input.csv](./documentation/example_inputs/preprocessing_input.csv)\n\nThe data can then be processed and split into training, validation and testing datasets of all\nvalid subsequences in the original data with the command:\n\n```console\nsequifier --preprocess --config_path=[CONFIG PATH]\n```\n\nThe config path specifies the path to the preprocessing config and the project\npath the path to the (preferably empty) folder the output files of the different\nsteps are written to.\n\nThe default config can be found on this path:\n\n[configs/preprocess.yaml](./configs/preprocess.yaml)\n\n\n\n#### Configuring and training the sequence classification model\n\nThe training step is executed with the command:\n\n```console\nsequifier --train --config_path=[CONFIG PATH]\n```\n\nIf the data on which the model is trained comes from the preprocessing step, the flag\n\n```console\n--on-preprocessed\n```\n\nshould also be added.\n\nIf the training data does not come from the preprocessing step, both train and validation\ndata have to take the form of a csv file with the columns "sequenceId", "subsequenceId", "col_name", [SEQ LENGTH], [SEQ LENGTH - 1],...,"1", "target".\nYou can find an example of the preprocessing input data at [documentation/example_inputs/training_input.csv](./documentation/example_inputs/training_input.csv)\n\nThe training step is configured using the config. The two default configs can be found here:\n\n[configs/train.yaml](./configs/train.yaml)\n\n[configs/train-on-preprocessed.yaml](./configs/train-on-preprocessed.yaml)\n\ndepending on whether the preprocessing step was executed.\n\n\n#### Inferring on test data using the trained model\n\nInference is done using the command:\n\n```console\nsequifier --infer --config_path=[CONFIG PATH]\n```\n\nand configured using a config file. The default version can be found here:\n\n[configs/infer.yaml](./configs/infer.yaml)\n\n\n',
    'author': 'Leon Luithlen',
    'author_email': 'leontimnaluithlen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/0xideas/sequifier',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
