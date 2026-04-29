from classification import linear_cl
from classification import multinomial_cl
from feature_extraction import simple_feature_extraction
from feature_extraction import function_words_extraction

def ngram_turning(classification_func, cleaned_articles, author_dict, ngram_lower, ngram_upper):
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
                f1 = average_performance(classification_func, cleaned_articles, author_dict, ngram_lower, ngram_upper)
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


