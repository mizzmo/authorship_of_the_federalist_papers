# Measuring For:
# Average number of words per sentence
# Sentence Length and Variation
# Lexical Diversity
# Can test for only Function words and All Words to see if there is a difference.
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt_tab')

from process_fed import get_federalist_dict

def average_words():
    federalist_dict, author_dict = get_federalist_dict()
    # Get each article.
    for article_number, article in federalist_dict.items():
        # Split the article into sentences.
        all_sentences = sent_tokenize(article)
        # Break down each sentence into words, remove punctuation.
        for sentence in all_sentences:
            words = word_tokenize(sentence)
            print(words)
            # NOTE Do something to disregard the first couple sentences as they are not part of the original papers / are repetitive.
        break
            
    # Calculate the average number of each sentence.
    
    # Produce metrics for each sentence
    
    # Corelate with names of Authors.
    
    # Produce separate results for each of the disputed papers
    
    # Overlay the results with the average for each author.    
    
# Graph the results by name
average_words()