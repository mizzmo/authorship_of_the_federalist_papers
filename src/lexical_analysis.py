# Measuring For:
# Average number of words per sentence
# Sentence Length and Variation
# Lexical Diversity
# Analyse the percentage chance that each author uses a specific type of punctuation.
# Can test for only Function words and All Words to see if there is a difference.
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt_tab')

from process_fed import get_federalist_dict

def clean_word_token(token: str):
    # Remove whitespace
    token = token.strip()
    # Remove tokens that are just numbers or punctuation.
    if token.isdigit():
        return None
    else:
        word = ""
        punctuation = {}
        # Split the token into individual characters
        letters = list(token)
        # Check each character to be a letter.
        for letter in letters:
            if letter.isalpha():
                # Add the letter to the word if it is alphanumerical
                word = word + letter
            # If the letter is not a number
            elif not letter.isdigit():
                # Add it to the tally.
                if letter in punctuation:
                    punctuation[letter] += 1
                else:
                    punctuation[letter] = 0
                
        return word, punctuation
        

def average_words():
    federalist_dict, author_dict = get_federalist_dict()
    # Get each article.
    for article_number, article in federalist_dict.items():
        # Split the article into sentences.
        all_sentences = sent_tokenize(article)
        # Break down each sentence into words, remove punctuation.
        for sentence in all_sentences:
            words = word_tokenize(sentence)
            to_remove = []
            # Process each word, note down any that are to be removed and remove after processing the entire array.
            for i in range(len(words)):
                cleaned_word = clean_word_token(words[i])
                if cleaned_word == None:
                    to_remove.append(i)
                else:
                    words[i] = cleaned_word
            # Remove the words marked for deletion
            print(to_remove)
            print(len(words))
            # Sort the list in reverse order and remove from back to front to prevent index error.
            for index in sorted(to_remove, reverse=True):
                words.pop(index)
                
            print(words)
        break
            
    # Calculate the average number of each sentence.
    
    # Produce metrics for each sentence
    
    # Corelate with names of Authors.
    
    # Produce separate results for each of the disputed papers
    
    # Overlay the results with the average for each author.    
    
# Graph the results by name
average_words()