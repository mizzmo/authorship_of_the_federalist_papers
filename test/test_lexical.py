from src.lexical_analysis import calculate_average_words
from src.lexical_analysis import clean_word_token

def test_average_sentences():
    # Define test sentences
    sentences = [["This", "is", "a", "sentence"], ["This", "is", "a", "sentence"], ["This", "is", "a", "sentence"]]
    # Average of the test is (4 + 4 + 4 / 3 = 4)
    calculated_average = calculate_average_words(sentences)
    assert calculated_average == 4, "Average Calculation is Incorrect."
    
def test_average_no_sentences():
    sentences = []
    calculated_average = calculate_average_words(sentences)
    assert calculated_average == 0, "Incorrect handling of 0 sentences."
    

def test_clean_tokens():
    # Confirm that tokens are being processed correctly.
    token = " Test-Token. "
    cleaned_token, punctuation = clean_word_token(token)
    assert cleaned_token == "testtoken"
    assert punctuation == {'.' : 1, '-' : 1}
    

def test_empty_clean_token():
    token = ""
    cleaned_token, punctuation = clean_word_token(token)
    assert cleaned_token == None
    assert punctuation == None
    
    
def test_punc_only_token():
    token = "!!!@@@@"
    cleaned_token, punctuation = clean_word_token(token)
    assert cleaned_token == None
    assert punctuation == {'!' : 3, '@' : 4}
    

def test_number_only_token():
    token = "12345"
    cleaned_token, punctuation = clean_word_token(token)
    assert cleaned_token == None
    assert punctuation == None
    
    
def test_number_and_letter_token():
    token = "4 Times."
    cleaned_token, punctuation = clean_word_token(token)
    assert cleaned_token == "times"
    assert punctuation == {'.' : 1}