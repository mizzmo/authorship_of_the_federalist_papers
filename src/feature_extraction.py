import pandas as pd
from process_fed import get_federalist_dict
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('universal_tagset')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer as wnl   
from nltk.tag import pos_tag
from sklearn.feature_extraction.text import CountVectorizer
# Bag of words model.

def convert_tags(input_tag):
    if input_tag.startswith('J'):
        return wordnet.ADJ
    elif input_tag.startswith('V'):
        return wordnet.VERB
    elif input_tag.startswith('N'):
        return wordnet.NOUN
    elif input_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


# Pre preparation
def pre_prep():
    cleaned_articles = {}
    federalist_articles, author_dict = get_federalist_dict()
    
    # Remove non alphabet characters, all lowercase
    for num, article in federalist_articles.items():  
        cleaned_articles[num] = (re.sub('[^A-Za-z]', ' ', article)).lower()
        
    # 1: Tokenization
    tokenized_articles = {}
    for num, article in cleaned_articles.items():
        # Tokenize each article (creates arrary of words)
        tokenized = word_tokenize(article)
        # Remove Stopwords
        stopwords_removed = []
        for word in tokenized:
            if word not in stopwords.words('english'):
                stopwords_removed.append(word)
        
        # POS Tagging
        pos_tagged = []
        pos_tagged = pos_tag(stopwords_removed, tagset='universal')
        
        
        # Lemmatization
        lemmatized = []
        for pos in pos_tagged:
            # Convert to correct tags for WordNet
            lemmatizer = wnl()
            lemma = lemmatizer.lemmatize(pos[0], convert_tags(pos[1]))
            lemmatized.append(lemma)
            
        # Add back to overall dictionary as one sentence.
        tokenized_articles[num] = " ".join(lemmatized)
    
    # 2: Count Vectorization - Create a Document Term Matrix by counting how many times a word from the vocab appears in a document.
    matrix = CountVectorizer(max_features=1000)
    for article in tokenized_articles.values():  
        print(article)
        x = matrix.fit_transform(article).toarray()
        print(x)


pre_prep()