import numpy as np

def create_input_pairs(pp_corpus, word2idx, context_size=2):
    """
    Create pairs of context and target words for training a Word2Vec model.

    Parameters
    ----------
    pp_corpus : list of list of str
        The preprocessed corpus where each document is a list of words.
    word2idx : dict
        A dictionary that maps words to their corresponding indices in the vocabulary.
    context_size : int, optional
        The number of context words to consider on either side of the target word (default is 2).

    Returns
    -------
    numpy.ndarray
        An array of pairs of context and target word indices.
    """
    if not isinstance(pp_corpus, list) or not all(isinstance(sentence, list) for sentence in pp_corpus):
        raise ValueError("pp_corpus must be a list of lists of strings.")
    if not isinstance(word2idx, dict) or not all(isinstance(word, str) for word in word2idx.keys()):
        raise ValueError("word2idx must be a dictionary mapping strings to integers.")
    if not isinstance(context_size, int) or context_size < 0:
        raise ValueError("context_size must be a non-negative integer.")
    idx_pairs = [(word2idx[sentence[i]], word2idx[sentence[j]])
                 for sentence in pp_corpus
                 for i in range(len(sentence))
                 for j in range(max(i - context_size, 0), min(i + context_size + 1, len(sentence)))
                 if i != j]
    return np.array(idx_pairs)

def get_vocab(tokenized_corpus):
    """
    Get the vocabulary from a tokenized corpus.

    Parameters
    ----------
    tokenized_corpus : list of list of str
        The tokenized corpus where each document is a list of words.

    Returns
    -------
    list
        The list of unique words in the corpus.
    """
    if not isinstance(tokenized_corpus, list) or not all(isinstance(sentence, list) for sentence in tokenized_corpus):
        raise ValueError("tokenized_corpus must be a list of lists of strings.")
    
    return list(set(token for sentence in tokenized_corpus for token in sentence))

def get_word_vectors(model, word2idx):
    """
    Get the word vectors from a trained Word2Vec model.

    Parameters
    ----------
    model : SkipgramModel
        The trained Word2Vec model.
    word2idx : dict
        A dictionary that maps words to their corresponding indices in the vocabulary.

    Returns
    -------
    dict
        A dictionary that maps words to their corresponding word vectors.
    """
    if not isinstance(word2idx, dict) or not all(isinstance(word, str) for word in word2idx.keys()):
        raise ValueError("word2idx must be a dictionary mapping strings to integers.")
    if not hasattr(model, 'embeddings') or not hasattr(model.embeddings, 'weight'):
        raise ValueError("Invalid model provided. Model must have 'embeddings' with 'weight' attribute.")
    
    embedding_weights = model.embeddings.weight.data
    word_vectors = {word: embedding_weights[idx].numpy() for word, idx in word2idx.items()}
    return word_vectors
