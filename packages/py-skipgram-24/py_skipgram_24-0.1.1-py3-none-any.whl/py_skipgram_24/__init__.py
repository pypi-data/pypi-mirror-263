# read version from installed package
from importlib.metadata import version
__version__ = version("py_skipgram_24")


from .py_skipgram_24 import SkipgramModel, train_model
from .utils import create_input_pairs, get_vocab, get_word_vectors
from .preprocessor import MyPreprocessor
