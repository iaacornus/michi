import wikipediaapi
import urllib.request
import enchant

import requests
import random
from bs4 import BeautifulSoup as bs

def give_topic():
    
    while True:
        sections = ["space", "health", "planet-earth", "strange-news", "animals", "history"]
        link = "https://www.livescience.com/" + random.choice(sections)
        page = requests.get(link)

        if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
            return False
            
        else:
            soup = bs(page.content, "html.parser")
            topics = (soup.find_all("h3", class_="article-name"))

            topic = str(random.choice(topics))[25:-5]
            for x in range(10):
                if ("top" or str(x) or "top " + str(x) or "best") in str(topic):
                    continue
                
                else :
                    return topic
    


def get_defin(define):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(define)

    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    comb = []
    for x in ALPHA:
        for y in alpha:
            comb.append(x+y)

    if page_py.exists() is True:
        defi = f"{str(page_py.summary)}"
        url = f"Full URL = {page_py.fullurl}\nCanonical URL = {page_py.canonicalurl}"
        
        return defi, url
    else:
        if (define[0].upper()+define[1].lower()) not in comb:
            return "the given term is not in Wikipedia, kindly correct the term and try again.", 0
        else:
            wiki = "https://en.wikipedia.org/wiki/Special:AllPages/" + define[0].upper() + define[1].lower()
            
            if urllib.request.urlopen(wiki).getcode() not in [x for x in range(200, 299)]:
                return "the source is unfortunately down ...", 0
            else:
                lang = enchant.Dict("en_US")
                lang.check(define)

                return f"maybe you mean {str(lang.suggest(define)).replace('[', '').replace(']', '')}", 0
              
