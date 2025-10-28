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
        return None, None
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
                    punctuation[letter] = 1
        if len(word) > 0:
            return word, punctuation
        else:
            return None, punctuation
        

def process_sentences(article):

    # Split the article into sentences.
    all_sentences = sent_tokenize(article)
    # Break down each sentence into words, remove punctuation.
    output_array = []
    output_punctuation = {}
    for sentence in all_sentences:
        words = word_tokenize(sentence)
        to_remove = []
        # Process each word, note down any that are to be removed and remove after processing the entire array.
        for i in range(len(words)):
            cleaned_word, token_punctuation = clean_word_token(words[i])
            if cleaned_word == None:
                to_remove.append(i)
            else:
                words[i] = cleaned_word
                
            # Tally up the punctuation for each sentence.
            if token_punctuation:
                for punctuation in token_punctuation:
                    if punctuation in output_punctuation:
                        output_punctuation[punctuation] += 1
                    else:
                        output_punctuation[punctuation] = 1
        # Remove the words marked for deletion
        # Sort the list in reverse order and remove from back to front to prevent index error.
        for index in sorted(to_remove, reverse=True):
            words.pop(index)
        
        # Add the processed sentence to the output array
        output_array.append(words)

        
    
    return output_array, output_punctuation
                

def average_words():
    # Calculate the average number of each sentence.
    
    # Produce metrics for each sentence
    
    # Corelate with names of Authors.
    
    # Produce separate results for each of the disputed papers
    
    # Overlay the results with the average for each author.    
    return
    
# Graph the results by name

# Get the initial dictionary.
federalist_dict, author_dict = get_federalist_dict()

# Get each article.
for article_number, article in federalist_dict.items():
    print("ARTICLE NUMBER:", article_number)
    sentences, punctuation = process_sentences(article)
    print(sentences)
    print("\n")
    print(punctuation)
    break


average_words()