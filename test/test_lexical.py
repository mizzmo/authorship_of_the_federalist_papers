from lexical_analysis import calculate_average_words
from lexical_analysis import clean_word_token
from lexical_analysis import process_sentences

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
    
    
def test_process_sentences():
    sentences = "16-Times the detail. 4-Times the size of FALLOUT 4!"
    processed_sents, processed_punc = process_sentences(sentences)
    assert processed_sents == [["times", "the", "detail"],["times", "the", "size", "of", "fallout"]]
    assert processed_punc == {'-' : 2, '.' : 1, '!' : 1}
    
    
def test_process_sentences_no_sentence():
    sentences = ""
    processed_sents, processed_punc = process_sentences(sentences)
    assert processed_sents == []
    assert processed_punc == {}
    
    
def test_process_sentences_numbers():
    sentences = "123456. 54321"
    processed_sents, processed_punc = process_sentences(sentences)
    assert processed_sents == []
    assert processed_punc == {'.' : 1}