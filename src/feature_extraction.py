import pandas as pd
from process_fed import get_federalist_dict
import re


def simple_feature_extraction():
    cleaned_articles = {}
    federalist_articles, author_dict = get_federalist_dict()

    # Remove non alphabet characters, all lowercase
    for num, article in federalist_articles.items():  
        cleaned_articles[num] = (re.sub('[^A-Za-z]', ' ', article)).lower()
    
    return cleaned_articles, author_dict



'''
MultinomialNB
Paper 18 predicted author: MADISON
Paper 19 predicted author: HAMILTON
Paper 20 predicted author: HAMILTON
Paper 49 predicted author: MADISON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: MADISON
Paper 55 predicted author: MADISON
Paper 56 predicted author: HAMILTON
Paper 57 predicted author: MADISON
Paper 58 predicted author: MADISON
Paper 64 predicted author: HAMILTON
Validation accuracy: 0.8666666666666667

LinearSVC
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: HAMILTON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: HAMILTON
Paper 55 predicted author: HAMILTON
Paper 56 predicted author: HAMILTON
Paper 57 predicted author: MADISON
Paper 58 predicted author: MADISON
Paper 64 predicted author: HAMILTON
Validation accuracy: 0.7333333333333333
'''