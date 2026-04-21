from classification import linear_cl
from classification import multinomial_cl
from feature_extraction import simple_feature_extraction

def ngram_turning():
    return


def average_accuracy(classification_func, cleaned_articles, author_dict, ngram_lower, ngram_upper, iterations = 50):
    # Runs the anaylsis x amount of times, keeps track of the average accuracy.
    average = 0
    for i in range(0, iterations):
        print(f"Iteration: {i}/{iterations} ------")
        accuracy = classification_func(cleaned_articles, author_dict, ngram_lower, ngram_upper)
        average += accuracy
    
    average /= iterations
    percentage = round(average, 5) * 100
    print(f"Average Accuracy: {percentage}%")
    return average


cleaned_articles, author_dict = simple_feature_extraction()
average_accuracy(multinomial_cl, cleaned_articles, author_dict, 3, 5)
        
        
# 50 Iterations of Linear - Average 83.467%% Accuracy.
# 50 Iterations of Multinomial - Average 83.333% Accuracy.