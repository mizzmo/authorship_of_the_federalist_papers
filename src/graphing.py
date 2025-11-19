import matplotlib.pyplot as plt
import pandas as pd

def plot_averages(averages, disputed_averages):
    plt.close("all")
    # Combine the two dictionaries
    averages.update(disputed_averages)
    
    #  Create a DataFrame where Authors/Articles are the index and the average is the first column
    frame = pd.DataFrame.from_dict(averages, orient='index', columns=['Average Words Per Sentence'])
    print (frame)
    
    # Convert the index (Authors/Articles) into a column
    frame = frame.reset_index()
    
    # Rename the column containing the Authors/Articles
    frame = frame.rename(columns={'index': 'Author / Article'})
    
    frame.plot(kind="bar", x='Author / Article', y='Average Words Per Sentence', rot=90) 
    plt.tight_layout() 
    plt.savefig("average_words.png")
    
    
def plot_punctuation(punctuation, disputed_punctuation):
    pass