from math import sqrt
import pandas as pd
# Euclidean Distance
# Square root of the Sum of every difference between each punctuation type on an article scope against the whole paper scope for an author squared.


def format_result(euclidean_result):
    # Convert to dataframe
    df = pd.DataFrame.from_dict(euclidean_result)
    # Add a new column which shows the closest match (lowest value)
    df['Best Match'] = df.idxmin(axis = 1)
        
    # Store the result in a txt file
    with open('src/punc_graphs/euclidean_dist.txt', 'w') as f:
        f.write(df.to_string())


def sqr_difference(x, y):
    # Square the difference in values.
    diff = abs(x - y)
    return diff * diff


def euclidean_distance(total_punctuation, disputed_punctuation):
    output = {}
    
    # For every author, and every disputed article, for the punctuation used in the authors work,
    # take the square of the difference between that of the article and that of the entire paper and add to sum. 
    # Then square root the result.
    for author in total_punctuation.keys():
        author_punc = total_punctuation[author]
        distances = {}
        for article in disputed_punctuation.keys():
            # Running total
            total = 0
            # For every present punc type.
            article_punc = disputed_punctuation[article]
            
            for punctuation_type in author_punc.keys():
                # Check if punc appears in article.
                if punctuation_type in article_punc.keys():
                    total += sqr_difference(article_punc[punctuation_type], author_punc[punctuation_type])
                # Use 0 if doesn't appear.
                else:
                    total += sqr_difference(0.0, author_punc[punctuation_type])
            
            distances[article] = sqrt(total)
        output[author] = distances
            
    format_result(output) 
     
    return output



