import nltk
import numpy
import scipy
import sklearn
import pandas
import matplotlib

from federalist_authors_enum import FederalistAuthor

def parse_federalist():
    federalist_articles = {}
    with open("resources/the_federalist_papers.txt", "r") as file:
        articles = 0
        new_article = ""
        for line in file:
            # Finds the start of each article.
            if line.startswith("FEDERALIST"):
                # Save the previous article if it exists
                if new_article and articles > 0:
                    federalist_articles[articles] = new_article.strip()
                    
                articles += 1
                # Erase prev article
                new_article = ""
                # Skips the article number
                continue
            # Final line in The Federalist Papers
            elif(line.strip() == "PUBLIUS"):
                federalist_articles[articles] = new_article.strip()
            else:
                # Ignore blank lines
                if line.strip() == "":
                    continue
                else:
                    new_article +=  (" " + line.strip()).lower()
                    
    # Write with correct article number and attribution
    with open("resources/federalist_articles_cleaned.txt", "w") as file:
        for article_num, content in federalist_articles.items():
            if article_num in FederalistAuthor.HAMILTON.value:
                file.write(f"HAMILTON: {article_num}: {content}\n")
            elif article_num in FederalistAuthor.MADISON.value:
                file.write(f"MADISON: {article_num}: {content}\n")
            elif article_num in FederalistAuthor.JAY.value:
                file.write(f"JAY: {article_num}: {content}\n")
            elif article_num in FederalistAuthor.DISPUTED.value:
                file.write(f"DISPUTED: {article_num}: {content}\n")
            else:
                file.write(f"UNKNOWN: {article_num}: {content}\n")
            
def make_dict():
    federalist_articles = {}
    try:
        parse_federalist()
        print(f"Parsed {len(federalist_articles)} articles.")
        return federalist_articles
    except Exception as e:
        print(f"Error parsing articles: {e}")
        return None
        
        
def check_federalist_dict():
    federalist_articles = {}
    try:
        with open("resources/federalist_articles_cleaned.txt", "r") as file:
            for line in file:
                # Try to load the dictionary from the cleaned file
                raw_article = line.split(": ", 2)
                federalist_articles[int(raw_article[1])] = raw_article[2].strip()
            if len(federalist_articles) != 85:
                print(f"Warning: Expected 85 articles, found {len(federalist_articles)}.")
                return None
            else:
                print("All articles successfully parsed.")
                return federalist_articles
        
    except Exception as e:
        print(f"Error reading federalist articles: {e}")
        return None
                
            
def get_federalist_dict():
    # Get the corpus dictionary.
    federalist_articles = check_federalist_dict()
    if federalist_articles == None:
        print("Dictionary Load Unsuccessful, Re-parsing document.")
        # Parse the original file again
        parse_federalist()
        # Try again to read the cleaned file
        federalist_articles = check_federalist_dict()
        if federalist_articles == None:
            print("Error: Could not parse federalist articles.")
            return None
        else:
            print("Dictionary Load Successful.")
            return federalist_articles
    else:
        print("Dictionary Load Successful.")
        return federalist_articles
    
        
            

get_federalist_dict()