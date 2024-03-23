# py_skipgram_24
![ci-cd](https://github.com/billwan96/2024_03-skipgram/actions/workflows/ci-cd.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/py-skipgram-24.svg)](https://badge.fury.io/py/py-skipgram-24)

## 📄 About
This package, named “py_skipgram_24”, is a comprehensive toolkit for Skip-gram modeling and evaluation. It offers a set of functions designed to facilitate various aspects of working with Skip-gram algorithms, from preprocessing the data, creating input pairs, training the model to getting word vectors. We aim to simplify the process by providing essential functionalities for data manipulation, model training, and evaluation.

## 📦 Functions
This package consists of six functions and explained as below:

- SkipgramModel(vocab_size, embedding_dim): This class initializes the Skipgram model with the vocabulary size and embedding dimension, and defines the forward pass.
- MyPreprocessor(texts, stopwords, strip_puncts=True): This class preprocesses the given texts by tokenizing the sentences, converting to lower case, and removing stopwords and punctuation.
- create_input_pairs(pp_corpus, word2idx, context_size=2): This function creates input pairs for the Skipgram model from the preprocessed corpus, word-to-index mapping, and context size.
- get_vocab(tokenized_corpus): This function gets the vocabulary from the tokenized corpus.
- get_word_vectors(model, word2idx): This function gets the word vectors from the trained model and word-to-index mapping.

## 🛠️ Installation
Option 1 (For Users)

The package has been published to PYPI, we could use pip install

Create and activate a virtual environment using conda
```
$ conda create --name <env_name> pip -y
$ conda activate <env_name>
```

Install the package using the command below
```
$ pip install py_skipgram_24
```

Option 2 (For Developers)

To successfully run the following commands of installation, we would need conda and poetry, guide included in the link (conda, poetry)

Clone this repository
```
$ git clone git@github.com:<your_username>/py_skipgram_24.git
```

Direct to the root of this repository
Create a virtual environment in Conda with Python by the following commands at terminal and activate it:
```
$ conda create --name py_skipgram_24 python=3.11 -y
$ conda activate py_skipgram_24
```

Install this package via poetry, run the following command.
```
$ poetry install
```

## ✅ Testing
To test this package, please run the following command from the root directory of the repository:
```
$ pytest tests/
```
Branch coverage could be viewed with the following command:
```
$ pytest --cov-branch --cov=py_skipgram_24
```

## Usage
To successfully use our Skipgram model to predict the target, please first ensure you have followed the instruction of installation, and then run the following line in a python notebook. Or you can look at the doc folder, with an example notebook.

```{python}
from py_skipgram_24 import SkipgramModel, create_input_pairs, get_vocab, MyPreprocessor, get_word_vectors
corpus = ["It was a great day. I loved the movie and spending time with you. I wish we had more time.", 
          "The sky is always blue underneath. Remember that."]
sentences = MyPreprocessor(corpus)
pp_corpus = list(sentences)
vocab = get_vocab(pp_corpus)
word2idx = {word: idx for idx, word in enumerate(vocab)}
idx_pairs = create_input_pairs(pp_corpus, word2idx, context_size=2)
model = SkipgramModel(len(vocab), 10)
train_model(model, idx_pairs, epochs=250, learning_rate=0.025)
word_vectors = get_word_vectors(model, word2idx)
print(word_vectors)
```

### 📚 Package Integration within the Python Ecosystem
py_skipgram_24, while acknowledging the robustness and the capabilities of PyTorch’s nn.Module, aims to offer a specialized and streamlined toolkit tailored explicitly for Skip-gram tasks. As a lightweight and focused alternative, py_skipgram_24 serves users who seek a concise package that offers preprocessing, creating input pairs, training the model, and getting word vectors functions. While PyTorch covers a broader spectrum of deep learning algorithms, py_skipgram_24 provides a more specialized package, potentially appealing to those who prefer a tailored implementation of their Skip-gram workflows.

### Contributing
Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License
`py_skipgram_24` was created by Bill. It is licensed under the terms of the MIT license.

## Credits
`py_skipgram_24` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
