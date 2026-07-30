import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    idx = {word: i for i, word in enumerate(vocab)}
    out = np.zeros(len(vocab), dtype=int)
    for token in tokens:
        if token in vocab:
            out[idx[token]]+=1
    return out
    