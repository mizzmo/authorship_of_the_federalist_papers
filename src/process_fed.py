import nltk
import numpy
import scipy
import sklearn
import pandas
import matplotlib

federalist_articles = {}

with open("resources/the_federalist_papers.txt", "r") as file:
    articles = 0
    new_article = ""
    for line in file:
        # Finds the start of each article.
        if line.startswith("FEDERALIST"):
            # Save the previous article if it exists
            if new_article:
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

print(federalist_articles[64])
          

   
            

