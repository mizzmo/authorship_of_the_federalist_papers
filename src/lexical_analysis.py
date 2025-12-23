# Measuring For:
# Average number of words per sentence
# Sentence Length and Variation
# Lexical Diversity
# Analyse the percentage chance that each author uses a specific type of punctuation.
# Can test for only Function words and All Words to see if there is a difference.
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd

nltk.download('punkt_tab')

from process_fed import get_federalist_dict
from federalist_authors_enum import FederalistAuthor
from graphing import plot_averages, plot_punctuation
from euclidean_distance import euclidean_distance

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
    word_count = 0
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
                word_count += 1
                
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
            word_count -= 1
        
        # Add the processed sentence to the output array
        if len(words) > 0:
            output_array.append(words)

    # Normalize the punctuation data by dividing by the total number of words in the article.
    for key, value in output_punctuation.items():
        output_punctuation[key] = value / word_count
    
    #print(output_punctuation)
    
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
    
def additive_combine_dictionaries(target_dict, source_dict):
    # Combine dictionaries by adding the values of the source to the values in the target.
    for key, value in source_dict.items():
        if type(value) == float:
            # Check if the key is in the target
            if key in target_dict.keys():
                # Update the value by adding the source.
                target_dict[key] = target_dict[key] + value
            else:
                # Create a new key in the target.
                target_dict[key] = value
        else:
            return {}
            
    return target_dict
    

def format_averages(average_words, author_dict):
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
            
    return total_averages, disputed_averages
            
            
def format_punctuation(punctuation_per_article, author_dict):
    # For each article, form lists of normalized punctuation appearances for each type of punctuation.
    average_punctuations = {"HAMILTON" : {}, "JAY" : {}, "MADISON" : {}}
    disputed_averages = {}
    for article_number, punctuation_dict in punctuation_per_article.items():
        # Find the author of the article in question
        author = author_dict[article_number]
        if author != "DISPUTED":            
            if author in average_punctuations.keys():
                for punctuation, average in punctuation_dict.items():
                    if punctuation in average_punctuations[author].keys():
                        average_punctuations[author][punctuation].append(average)
                    else:
                        average_punctuations[author][punctuation] = [average]
        else:
            disputed_averages[article_number] = punctuation_dict
    
    
    output_dict = {"HAMILTON" : {}, "JAY" : {}, "MADISON" : {}}
    # For each author, work out the average of all normalised punctuation appearances.
    for author in average_punctuations.keys():
        for punctuation_type, averages in average_punctuations[author].items():
            total = 0
            for value in averages:
                total += value
            average_norm = total / len(averages)
            # Average per 100 words
            average_norm *= 100
            output_dict[author][punctuation_type] = average_norm
            
    for article, punc_array in disputed_averages.items():
        for punctuation in punc_array:
            # Multiply by 100 to be per 100 words.
            disputed_averages[article][punctuation] = disputed_averages[article][punctuation] * 100
        
    return output_dict, disputed_averages


def absolute_difference(author_averages, disputed_dicts):
    # Calculate the absolute difference between the mean of each type of punctuation and the mean of every disputed punctuation.
    # Store the values for TAD and individual AD for every disputed article and each contained punctuation type.
    results_by_article = {}

    # Iterate over each disputed article 
    for article, article_data in disputed_dicts.items():
        # Dictionary to store differences for the current article
        article_differences = {}
        total_absolute_difference = 0
        # Iterate over the author's mean punctuation
        for punc, mean_value in author_averages.items():
            
            # Check if the punctuation is present in the current article
            if punc in article_data:
                article_frequency = article_data[punc]
                
                # Calculate Absolute Difference: |X - μ|
                absolute_diff = abs(article_frequency - mean_value)
                
                article_differences[punc] = absolute_diff
                # Sum the differences for Total Absolute Difference, TAD
                total_absolute_difference += absolute_diff 
        
        # Store the total distance for this article against the current author
        article_differences['TAD'] = total_absolute_difference
        
        # Store the complete results for the article
        results_by_article[article] = article_differences
    return results_by_article
            

def main():    
    # Get the initial dictionary.
    federalist_dict, author_dict = get_federalist_dict()
    
    # Store the average number of words per article and total punctuation appearances per article.
    average_words, punctuation_per_article = {}, {}
    # Get each article.
    for article_number, article in federalist_dict.items():
        # Produce metrics for each sentence
        sentences, punctuation = process_sentences(article)
        # Add the average to the dictionary at corresponding article.
        average_words[article_number] = calculate_average_words(sentences)
        punctuation_per_article[article_number] = punctuation

    total_averages, disputed_averages = format_averages(average_words, author_dict)
    total_punctuation, disputed_punctuation = format_punctuation(punctuation_per_article, author_dict)
    # Plot the average data in a bar graph.
    #plot_averages(total_averages, disputed_averages)
    #plot_punctuation(total_punctuation, disputed_punctuation)
    
    # Euclidean Distance
    euclidean_values = euclidean_distance(total_punctuation, disputed_punctuation)
    
    pass
    combined_rows = []

    for author in total_punctuation.keys():
        result_dict = absolute_difference(total_punctuation[author], disputed_punctuation)
        
        # Convert dict → DF, orient so each disputed article becomes a row
        df = pd.DataFrame.from_dict(result_dict, orient='index')
        
        # Label rows with the author
        df['author'] = author
        
        combined_rows.append(df)

    # Final combined dataframe
    data_frame = pd.concat(combined_rows).reset_index().rename(columns={'index': 'article'})
    1000
    # Write to file
    with open('src/punc_graphs/total_absolute_difference_raw.txt', 'w') as f:
        f.write(data_frame.to_string())
    
    # Create the wide comparison table using only the TAD column
    df_comparison = data_frame.pivot(index='article', columns='author', values='TAD')

    # Rename columns
    df_comparison.columns = [f'{col}_TAD' for col in df_comparison.columns]
    
    # Find the author with the lowest TAD, hence the most similar.
    # Find all TAD Columns.
    tad_columns = df_comparison.filter(like="TAD").columns
    # Add a column to hold the best match.
    # Find the column name of the column holding the minimum value in that row.
    df_comparison['Best Match'] = df_comparison[tad_columns].idxmin(axis = 1)
    # Replace TAD with nothing to clean up the output.
    df_comparison['Best Match'] = df_comparison['Best Match'].str.replace('_TAD', '')
    
    # Store the result in a txt file
    with open('src/punc_graphs/total_absolute_difference.txt', 'w') as f:
        f.write(df_comparison.to_string())


main()

# TODO Need to normalize the data as it means nothing in the current context.
# TODO Normalize punctuation by dividing each data point by the number of words in the associated sentence. This gets a more fair comparison between sentences.
# TODO Use Euclidean Distance and Cosine Similarity to compare data between authors. Doing this gets a more useful distance score for comparison.
# TODO Visualize the data using Principal Component Analysis (PCA) to get a better grasp of where the data falls when in 2D space.