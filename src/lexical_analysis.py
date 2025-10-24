# Measuring For:
# Average number of words per sentence
# Sentence Length and Variation
# Lexical Diversity
# Can test for only Function words and All Words to see if there is a difference.

from process_fed import get_federalist_dict

def average_words():
    federalist_dict, author_dict = get_federalist_dict()
    print(author_dict)
    
average_words()