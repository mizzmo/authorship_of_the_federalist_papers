from math import sqrt
import pandas as pd
# Cosine similarity

def calc_magnitude(vector):
    # Take each punctuation usage, square them, add them together and square root the result.
    magnitude = 0
    running = 0
    for key in vector.keys():
        squared = vector[key] * vector[key]
        running += squared
    
    magnitude = sqrt(running)
    return magnitude


def cosine_similarity(total_punctuation, disputed_punctuation):
    output = {}
    # Remember to use the same number of punc when comparing and use 0 for missing.
    
    
