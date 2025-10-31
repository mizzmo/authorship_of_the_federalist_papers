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

from src.process_fed import get_federalist_dict

def clean_word_token(token: str):
    # Remove whitespace
    token = token.strip()
    # Convert to lowercase.
    token = token.lower()
    # Remove tokens that are just numbers
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
            # If the letter is not a number or whitespace
            elif not letter.isdigit() and not letter == ' ':
                # Add it to the tally.
                if letter in punctuation:
                    punctuation[letter] += 1
                else:
                    punctuation[letter] = 1
        if len(word) > 0:
            return word, punctuation
        elif len(punctuation) > 0:
            return None, punctuation
        else:
            return None, None
        

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
        if len(words) > 0:
            output_array.append(words)

        
    
    return output_array, output_punctuation
                

def calculate_average_words(sentences):
    running_total = 0
    # Calculate the average number of each sentence.
    for sentence in sentences:
        running_total += len(sentence)
    # Return the average number of words in all sentences.
    if len(sentences) != 0:
        return running_total / len(sentences)
    else:
        return 0
    
    
    
    
    
# Get the initial dictionary.
federalist_dict, author_dict = get_federalist_dict()

average_words = {}
# Get each article.
for article_number, article in federalist_dict.items():
    # Produce metrics for each sentence
    sentences, punctuation = process_sentences(article)
    # Add the average to the dictionary at corresponding article.
    average_words[article_number] = calculate_average_words(sentences)


# Corelate with names of Authors.
author_average = {"HAMILTON" : [], "JAY" : [], "MADISON" : []}
disputed_averages = {}
# Using the author dictionary, work out the average number of words per sentence for each author.
for article_number, word_average in average_words.items():
    # Find the author of that article.
    author = author_dict[article_number]
        # Handle disputed articles separately.
    if author != "DISPUTED":
        # Add the average to that of the correct author.
        author_average[author].append(word_average)
    else:
        disputed_averages[article_number] = round(word_average, 2)

# Store averages
total_averages = {} 
# Go through each of the arrays, working out the average of the averages.
for author, average_array in author_average.items():
    running_total = 0
    for average in average_array:
        running_total += average
    
    if len(average_array) != 0:
        average_average = running_total / len(average_array)
        total_averages[author] = round(average_average, 2)
    else:
        total_averages[author] = 0.00


print(total_averages)
print(disputed_averages)

# Overlay the results with the average for each author.    
# Use a Plotting library to visualize the results.
