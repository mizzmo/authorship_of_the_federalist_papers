from src.lexical_analysis import calculate_average_words

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
    