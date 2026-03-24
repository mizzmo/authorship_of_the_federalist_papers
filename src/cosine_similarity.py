from math import sqrt
import pandas as pd
# Cosine similarity

def format_result(result_dict):
    # Convert to dataframe
    df = pd.DataFrame.from_dict(result_dict)
    # Add a new column which shows the closest match (highest value)
    df['Best Match'] = df.idxmax(axis = 1)
        
    # Store the result in a txt file
    with open('src/punc_graphs/cosine_dist.txt', 'w') as f:
        f.write(df.to_string())
            

def calc_magnitude(vector):
    # Take each punctuation usage, square them, add them together and square root the result.
    running = 0
    for key in vector.keys():
        squared = vector[key] * vector[key]
        running += squared
    
    magnitude = sqrt(running)
    return magnitude


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
            # Work out which punc is included in each and which should be a zero value. (Union)
            all_punc = set(disputed_punctuation[article].keys()) | set(total_punctuation[author].keys())
            # Work out dot product
            running = 0
            for punc in all_punc:
                v1 = disputed_punctuation[article].get(punc, 0)
                v2 = total_punctuation[author].get(punc, 0)
                running += v1 * v2
            
            # Calculate similarity by then dividing sum by the product of both magnitudes.
            similarity = running / (magnitude * disp_magnitude)
            # Add to output
            similarities[article] = similarity
        output[author] = similarities
    
    print(output)
    # Find the closest matches. 
    format_result(output)
    
    
