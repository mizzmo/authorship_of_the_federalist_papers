import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    plt.savefig("src/average_graphs/average_words.png")
    
    
def plot_punctuation(punctuation, disputed_punctuation):
    plt.close("all")
    # Combine the two dictionaries into a single dict
    punctuation.update(disputed_punctuation)
    
    data_frames = []
    # Create a separate dataframe for each author, where each punctuation type is on the x axis and the average usage is on the y axis.
    for key in punctuation.keys():
        # Create dataframe from dictionary.
        df = pd.DataFrame.from_dict(punctuation[key], orient='index', columns=['Average Appearances'])
        # Sort by highest to lowest average
        df = df.sort_values(by='Average Appearances', ascending=False)
        # Use the default dataframe index rather than using punctuation to index.
        df = df.reset_index()
        # Rename the column containing the punctuation accordingly.
        df = df.rename(columns={'index' : 'Character'})
        
        # Add author name
        df["Author"] = key
        
        # Add Dataframe to array.
        data_frames.append(df)
        # Plot a histogram based on the dataframe
        df.plot(kind='barh', x ='Character', y ='Average Appearances', title= 'Average Punctuation Usage Across All Articles: ' + str(key))
        plt.tight_layout() 
        # Save the plot with the correct name.
        plt.savefig("src/punc_graphs/average_punc_" + str(key) + ".png")
        
    # Combine all dataframes into a single dataframe.
    combined_df = pd.concat(data_frames, ignore_index=True)
    
    with open('src/punc_graphs/raw.txt', 'w') as f:
        f.write(combined_df.to_string())
    
    # Pivot to heatmap format
    heatmap_df = combined_df.pivot(index='Character', columns='Author', values='Average Appearances')
    
    # Plot a histogram based on the dataframe
    #combined_df.plot(kind='bar', x ='Character', y ='Average Appearances', title= 'Average Punctuation Usage Across All Articles and All Authors')
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_df, annot=True, fmt=".2f", cmap="Reds")
    # Sort heatmap by most frequently occurring punc
    heatmap_df = heatmap_df.loc[heatmap_df.mean(axis=1).sort_values(ascending=False).index]
    plt.title("Punctuation Usage Across Authors")
    plt.ylabel("Punctuation")
    plt.xlabel("Author")
    plt.tight_layout() 
    # Save the plot with the correct name.
    plt.savefig("src/punc_graphs/combined_average_punc.png")
    
        
    