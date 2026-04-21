from classification import linear_cl
from classification import multinomial_cl
from feature_extraction import simple_feature_extraction
from feature_extraction import function_words_extraction

def ngram_turning(classification_func):
    # Range of N-Grams, 1-5. Every combination to see best result.
    best_f1 = 0
    best_lower = 0
    best_upper = 0
    for lower_bound in range(1, 5):
        for upper_bound in range(1, 6):
            if upper_bound < lower_bound:
                continue
            else:
                print(f"Testing range {lower_bound} to {upper_bound}.")
                f1 = average_performance(classification_func, cleaned_articles, author_dict, lower_bound, upper_bound)
                if f1 > best_f1:
                    best_f1 = f1
                    best_lower = lower_bound
                    best_upper = upper_bound
    
    print(f"Best N-Gram Range: {best_lower} to {best_upper}: F1 Accuracy of {round((best_f1 * 100), 2)}%")


def average_performance(classification_func, cleaned_articles, author_dict, ngram_lower, ngram_upper, iterations = 20):
    # Runs the anaylsis x amount of times, keeps track of the average accuracy.
    acc_avrg = 0
    f1_avrg = 0
    for i in range(0, iterations):
        print(f"\nIteration: {i}/{iterations} ------")
        accuracy, f1 = classification_func(cleaned_articles, author_dict, ngram_lower, ngram_upper)
        acc_avrg += accuracy
        f1_avrg += f1
    
    acc_avrg /= iterations
    f1_avrg /= iterations
    acc_percentage = round(acc_avrg, 5) * 100
    f1_percentage = round(f1_avrg, 5) * 100
    print(f"Average Accuracy: {acc_percentage}%")
    print(f"Average F1: {f1_percentage}%")
    return f1_avrg





cleaned_articles, author_dict = simple_feature_extraction()
#cleaned_articles, author_dict = function_words_extraction()



ngram_turning(linear_cl)
#average_performance(multinomial_cl, cleaned_articles, author_dict, 2, 2)
        
        
# Linear 
# ACCURACY
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

# F1 SCORE

# Best Performing Ngram Range (4->4) for normal vocabulary - Average 71.59% F1 Score.

'''
Highest Performing Result
Iteration: 1/20 ------
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
Validation accuracy: 1.0
Validation F1: 1.0
'''

# Best Performing Ngram Range (4->5) for function word vocabulary - Average 78.99% F1 Score.
'''
Highest Performing Result
Iteration: 9/20 ------
LinearSVC
Paper 18 predicted author: MADISON
Paper 19 predicted author: MADISON
Paper 20 predicted author: MADISON
Paper 49 predicted author: HAMILTON
Paper 50 predicted author: MADISON
Paper 51 predicted author: MADISON
Paper 52 predicted author: HAMILTON
Paper 53 predicted author: MADISON
Paper 54 predicted author: MADISON
Paper 55 predicted author: HAMILTON
Paper 56 predicted author: MADISON
Paper 57 predicted author: HAMILTON
Paper 58 predicted author: MADISON
Paper 64 predicted author: JAY
Validation accuracy: 0.9333333333333333
Validation F1: 0.918840579710145
'''

# Multinomial
# ACCURACY
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

# F1 SCORE
# Best Performing Ngram Range (2->2) for normal vocabulary - Average 85.94% F1.

'''
Highest Performing Result
Iteration: 6/20 ------
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
Validation accuracy: 0.9333333333333333
Validation F1: 0.9365079365079364
'''

# Best Performing Ngram Range (4->4) for function word vocabulary - Average 86.57% F1.

'''
Highest Performing Result
Iteration: 1/20 ------
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
Validation F1: 1.0
'''