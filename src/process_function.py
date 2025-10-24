# Source of word list https://semanticsimilarity.wordpress.com/function-word-lists/

# Quick Script to process the list of function words I found.

import re 

with open("resources/function_words.txt", 'r') as file:
    words = []
    for line in file:
        line = line.strip()
        if not line.isalpha():
            new_line = re.sub(r'\d+', '', line)
            words.append(new_line)
        elif line.isalpha():
            words.append(line.strip())
        
    
with open("resources/function_words_clean.txt", 'w') as file:
    for word in words:
        file.write(word + "\n")
    
            