from classification import linear_cl
from classification import multinomial_cl
from feature_extraction import simple_feature_extraction
from feature_extraction import function_words_extraction

def ngram_turning(classification_func):
    # Range of N-Grams, 1-5. Every combination to see best result.
    best_accuracy = 0
    best_lower = 0
    best_upper = 0
    for lower_bound in range(1, 5):
        for upper_bound in range(1, 6):
            if upper_bound < lower_bound:
                continue
            else:
                print(f"Testing range {lower_bound} to {upper_bound}.")
                accuracy = average_accuracy(classification_func, cleaned_articles, author_dict, lower_bound, upper_bound)
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_lower = lower_bound
                    best_upper = upper_bound
    
    print(f"Best N-Gram Range: {best_lower} to {best_upper}: Accuracy of {round((best_accuracy * 100), 2)}%")


def average_accuracy(classification_func, cleaned_articles, author_dict, ngram_lower, ngram_upper, iterations = 20):
    # Runs the anaylsis x amount of times, keeps track of the average accuracy.
    average = 0
    for i in range(0, iterations):
        print(f"\nIteration: {i}/{iterations} ------")
        accuracy = classification_func(cleaned_articles, author_dict, ngram_lower, ngram_upper)
        average += accuracy
    
    average /= iterations
    percentage = round(average, 5) * 100
    print(f"Average Accuracy: {percentage}%")
    return average





cleaned_articles, author_dict = simple_feature_extraction()
#cleaned_articles, author_dict = function_words_extraction()



#ngram_turning(multinomial_cl)
average_accuracy(multinomial_cl, cleaned_articles, author_dict, 3, 5)
        
        
# Linear 
# 50 Iterations of Linear - Average 83.467%% Accuracy.
# Best Performing Ngram Range (4->4) for normal vocabulary - Average 85.33% Accuracy.

'''
Highest Performing Result
Iteration: 8/20 ------
LinearSVC
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: HAMILTON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: HAMILTON
Paper 55 predicted author: HAMILTON
Paper 56 predicted author: HAMILTON
Paper 57 predicted author: MADISON
Paper 58 predicted author: MADISON
Paper 64 predicted author: HAMILTON
Validation accuracy: 0.9333333333333333
'''

# Best Performing Ngram Range (4->5) for function word vocabulary - Average 87.00% Accuracy.

'''
Highest Performing Result
Iteration: 14/20 ------
LinearSVC
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: HAMILTON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: MADISON
Paper 55 predicted author: HAMILTON
Paper 56 predicted author: MADISON
Paper 57 predicted author: HAMILTON
Paper 58 predicted author: MADISON
Paper 64 predicted author: JAY
Validation accuracy: 0.9333333333333333
'''

# Multinomial
# 50 Iterations of Multinomial Ngram (3->5) - Average 83.333% Accuracy.
# Best Performing Ngram Range (1->2) for normal vocabulary - Average 92.33% Accuracy.

'''
Highest Performing Result
Iteration: 13/20 ------
MultinomialNB
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: MADISON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: MADISON
Paper 55 predicted author: MADISON
Paper 56 predicted author: MADISON
Paper 57 predicted author: MADISON
Paper 58 predicted author: MADISON
Paper 64 predicted author: HAMILTON
Validation accuracy: 1.0
'''


# Best Performing Ngram Range (2->4) for function word vocabulary - Average 96.67% Accuracy.

'''
Highest Performing Result
Iteration: 15/20 ------
MultinomialNB
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: MADISON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: MADISON
Paper 53 predicted author: MADISON
Paper 54 predicted author: MADISON
Paper 55 predicted author: MADISON
Paper 56 predicted author: MADISON
Paper 57 predicted author: MADISON
Paper 58 predicted author: MADISON
Paper 64 predicted author: MADISON
Validation accuracy: 1.0
'''
