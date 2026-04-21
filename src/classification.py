import nltk
nltk.download('punkt')

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

from feature_extraction import simple_feature_extraction

def get_train_test(cleaned_articles, author_dict):
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
            
    return train_texts, train_labels, test_texts, test_ids


def multinomial_cl(cleaned_articles, author_dict, ngram_lower, ngram_upper):
    

    train_texts, train_labels, test_texts, test_ids = get_train_test(cleaned_articles, author_dict)
    
    # Count Vectorization - Create a Document Term Matrix by counting how many times a word from the vocab appears in a document.
    vectorizer = CountVectorizer(
        analyzer='char',
        ngram_range=(ngram_lower, ngram_upper)
    )

    X_train = vectorizer.fit_transform(train_texts)
    X_test = vectorizer.transform(test_texts)
    print('MultinomialNB')
    # Multinomial Naive Bayes Classifier
    model = MultinomialNB()
    model.fit(X_train, train_labels)

    predictions = model.predict(X_test)

    #for i in range(len(test_ids)):
    #    print(f"Paper {test_ids[i]} predicted author: {predictions[i]}")
        
    #Validation
    X = vectorizer.fit_transform(train_texts)
    y = train_labels

    X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, stratify=y)

    model.fit(X_tr, y_tr)
    print("Validation accuracy:", model.score(X_val, y_val))

    accuracy = model.score(X_val, y_val)
    # Return the accuracy so I can analyse it after each iteration.
    return accuracy

def linear_cl(cleaned_articles, author_dict, ngram_lower, ngram_upper):
    
    print('LinearSVC')

    train_texts, train_labels, test_texts, test_ids = get_train_test(cleaned_articles, author_dict)

    vectorizer = TfidfVectorizer(
        analyzer='char',
        ngram_range=(ngram_lower,ngram_upper),
    )

    X_train = vectorizer.fit_transform(train_texts)
    X_test = vectorizer.transform(test_texts)

    model = LinearSVC(class_weight='balanced')
    model.fit(X_train, train_labels)

    predictions = model.predict(X_test)

    #for i in range(len(test_ids)):
    #    print(f"Paper {test_ids[i]} predicted author: {predictions[i]}")

    #Validation
    X = vectorizer.fit_transform(train_texts)
    y = train_labels

    X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, stratify=y)

    model.fit(X_tr, y_tr)
    print("Validation accuracy:", model.score(X_val, y_val))
    accuracy = model.score(X_val, y_val)
    # Return the accuracy so I can analyse it after each iteration.
    return accuracy
    
    
    
#cleaned_articles, author_dict = simple_feature_extraction()
#multinomial_cl(cleaned_articles, author_dict, 3, 5)
#linear_cl(cleaned_articles, author_dict, 3, 5)