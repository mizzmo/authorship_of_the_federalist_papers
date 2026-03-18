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

def find_matching_punc(dataset_1, dataset_2):
    # Make copies so we can remove items to improve efficiency.
    A = dataset_1.copy()
    B = dataset_2.copy()
    
    matches = []
    for key_A in A:
        if key_A in B.keys():
            matches.append(key_A)
    
    return matches
    


def cosine_similarity(total_punctuation, disputed_punctuation):
    # {Author {x,  article x similarity}, {...}}
    output = {}
    # Remember to use the same number of punc when comparing and use 0 for missing.
    # For each author
    for author in total_punctuation.keys():
        similarities = {}
        # Calculate the magnitude for that dataset.
        magnitude = calc_magnitude(total_punctuation[author])
        # For each of the disputed articles, calculate their magnitude.
        for article in disputed_punctuation.keys():
            disp_magnitude = calc_magnitude(disputed_punctuation[article])
            # Work out which punc is included in each and which should be a zero value.
            matches = find_matching_punc(disputed_punctuation[article], total_punctuation[author])
            # Multiply each type of matching punctuation and add it to sum.
            # If there is no match, treat as 0 (dont add it on)
            running = 0
            for punc in matches:
                multiply = disputed_punctuation[article][punc] * total_punctuation[author][punc]
                running += multiply
            
            # Calculate similarity by then dividing sum by the product of both magnitudes.
            similarity = running / (magnitude * disp_magnitude)
            # Add to output
            similarities[article] = similarity
        output[author] = similarities
    
    print(output)
    
    
