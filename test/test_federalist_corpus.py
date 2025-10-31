import process_fed as pf

def test_dict():
    dictionary = pf.get_federalist_dict()
    assert dictionary != None, "Dictionary does not exist."

def test_dict_len():
    dictionary, author_dict = pf.get_federalist_dict()
    assert len(dictionary) == 85, "Dictionary does not contain the correct number of articles."
    assert len(author_dict) == 85, "Author Dictionary does not contain the correct number of articles."