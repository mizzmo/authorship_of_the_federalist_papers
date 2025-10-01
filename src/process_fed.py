import nltk
import numpy
import scipy
import sklearn
import pandas
import matplotlib

federalist_articles = {}

def parse_federalist():
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
            else:
                # Ignore blank lines
                if line.strip() == "":
                    continue
                else:
                    new_article +=  (" " + line.strip()).lower()

    with open("resources/federalist_articles_cleaned.txt", "w") as file:
        for article_num, content in federalist_articles.items():
            file.write(f"{article_num}: {content}\n")       
            
def make_dict():
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
                raw_article = line.split(": ", 1)
                federalist_articles[int(raw_article[0])] = raw_article[1].strip()
            if len(federalist_articles) != 84:
                print(f"Warning: Expected 85 articles, found {len(federalist_articles)}.")
                parse_federalist()
                return None
            else:
                print("All articles successfully parsed.")
                return federalist_articles
        
    except Exception as e:
        print(f"Error reading federalist articles: {e}")
        return None
                
            
if __name__ == "__main__":
    federalist_articles = check_federalist_dict()
    if federalist_articles == None:
        print("No articles loaded.")
    else:
        print(f"Loaded {len(federalist_articles)+1} articles.")
        print(federalist_articles[84])
        
            

