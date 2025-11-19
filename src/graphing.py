import matplotlib.pyplot as plt
import pandas as pd

def plot_averages(averages, disputed_averages):
    plt.close("all")
    # Combine the two dictionaries
    averages.update(disputed_averages)
    
    #  Create a DataFrame where Authors/Articles are the index and the average is the first column
    frame = pd.DataFrame.from_dict(averages, orient='index', columns=['Average Words Per Sentence'])    
    
    # Convert the index (Authors/Articles) into a column
    frame = frame.reset_index()

    # Rename the column containing the Authors/Articles
    frame = frame.rename(columns={'index': 'Author / Article'})
        
    frame.plot(kind='bar', x='Author / Article', y='Average Words Per Sentence', rot=90) 
    plt.tight_layout() 
    plt.savefig("average_words.png")
    
    
def plot_punctuation(punctuation, disputed_punctuation):
    plt.close("all")
    # Combine the two dictionaries into a single dict
    punctuation.update(disputed_punctuation)
    
    data_frames = []
    # Create a separate dataframe for each author, where each punctuation type is on the x axis and the average usage is on the y axis.
    for key in punctuation.keys():
        # Create dataframe from dictionary.
        df = pd.DataFrame.from_dict(punctuation[key], orient='index', columns=['Average Appearances'])
        # Use the default dataframe index rather than using punctuation to index.
        df = df.reset_index()
        # Rename the column containing the punctuation accordingly.
        df = df.rename(columns={'index' : 'Character'})
        # Plot a histogram based on the dataframe
        df.plot(kind='barh', x ='Character', y ='Average Appearances', rot=90, title= 'Average Punctuation Usage Across All Articles: ' + str(key))
        plt.tight_layout() 
        # Save the plot with the correct name.
        plt.savefig("punc_graphs/average_punc_" + str(key) + ".png")
        
    