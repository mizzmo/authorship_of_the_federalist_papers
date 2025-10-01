from packaging import version

def test_dependencies():
    import numpy
    import scipy
    import sklearn
    import pandas
    import matplotlib
    import nltk

    assert version.parse(numpy.__version__) >= version.parse("2.3.3")
    assert version.parse(scipy.__version__) >= version.parse("1.16.2")
    assert version.parse(sklearn.__version__) >= version.parse("1.7.2")
    assert version.parse(pandas.__version__) >= version.parse("2.3.3")
    assert version.parse(matplotlib.__version__) >= version.parse("3.10.6")
    assert version.parse(nltk.__version__) >= version.parse("3.9.2")