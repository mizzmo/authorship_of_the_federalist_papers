import pandas as pd
from process_fed import get_federalist_dict
import re
import nltk
nltk.download('punkt')

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


cleaned_articles = {}
federalist_articles, author_dict = get_federalist_dict()

# Remove non alphabet characters, all lowercase
for num, article in federalist_articles.items():  
    cleaned_articles[num] = (re.sub('[^A-Za-z]', ' ', article)).lower()

# Split the input data into training and test sets
# Disputed articles should be used as test sets.

# Training Set (Non Disputed)
train_texts = []
train_labels = []
for num, article in cleaned_articles.items():
    if author_dict[num] != "DISPUTED":
        train_texts.append(article)
        train_labels.append(author_dict[num])

# Test Sets (Disputed)
test_texts = []
test_ids = []

for num, article in cleaned_articles.items():
    if author_dict[num] == "DISPUTED":
        test_texts.append(article)
        test_ids.append(num)

# Count Vectorization - Create a Document Term Matrix by counting how many times a word from the vocab appears in a document.
vectorizer = CountVectorizer(analyzer='char', ngram_range=(3,5))

X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

# Multinomial Naive Bayes Classifier
mnb = MultinomialNB()
mnb.fit(X_train, train_labels)

predictions = mnb.predict(X_test)

for i in range(len(test_ids)):
    print(f"Paper {test_ids[i]} predicted author: {predictions[i]}")
    
    
    

X = vectorizer.fit_transform(train_texts)
y = train_labels

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, stratify=y)

mnb.fit(X_tr, y_tr)
print("Validation accuracy:", mnb.score(X_val, y_val))
