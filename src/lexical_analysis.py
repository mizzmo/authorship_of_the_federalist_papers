# Measuring For:
# Average number of words per sentence
# Sentence Length and Variation
# Lexical Diversity
# Can test for only Function words and All Words to see if there is a difference.

from process_fed import get_federalist_dict

def average_words():
    federalist_dict, author_dict = get_federalist_dict()
    # Get each article.
    for article_number, article in federalist_dict.items():
    # Split the article into sentences.
        print(article_number)
        print(article)
    # Calculate the average number of each sentence.
    
    # Produce metrics for each sentence
    
    # Corelate with names of Authors.
    
    # Produce separate results for each of the disputed papers
    
    # Overlay the results with the average for each author.    
    
# Graph the results by name
average_words()