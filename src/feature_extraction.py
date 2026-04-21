import pandas as pd
from process_fed import get_federalist_dict
import re


import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize


def simple_feature_extraction():
    cleaned_articles = {}
    federalist_articles, author_dict = get_federalist_dict()

    # Remove non alphabet characters, all lowercase
    for num, article in federalist_articles.items():  
        cleaned_articles[num] = (re.sub('[^A-Za-z]', ' ', article)).lower()
    
    return cleaned_articles, author_dict

# Feature extraction using only function words.
def function_words_extraction():
    
    cleaned_articles = {}
    federalist_articles, author_dict = get_federalist_dict()
    
    
    # Get list of function words.
    function_words = []
    with open("resources/function_words_clean.txt", 'r') as f:
        # File already parsed into single word lines, so only need to remove new line characters
        function_words = [line.rstrip() for line in f]
        f.close()
    
    cleaned_tokens = {}
    for num, article in federalist_articles.items():  
        cleaned_tokens[num] = word_tokenize((re.sub('[^A-Za-z]', ' ', article)).lower())
    
    function_tokens = {}
    
    # Filter out any words that are not function words.
    for num, tokens in cleaned_tokens.items():
        c_function_words = []
        for token in tokens:
            if token in function_words:
                c_function_words.append(token)
        # Add list of function tokens to dictionary to associate with correct article
        function_tokens[num] = c_function_words
        # Join tokens for the current article and add to dictionary
        cleaned_articles[num] = " ".join(c_function_words)
        
    return cleaned_articles, author_dict


function_words_extraction()
    
            