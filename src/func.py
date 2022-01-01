import wikipediaapi
import urllib.request
import enchant

import requests
import random
from bs4 import BeautifulSoup as bs

import json
import re

def give_topic():
    
    while True:
        sections = ["space", "health", "planet-earth", "strange-news", "animals", "history"]
        link = "https://www.livescience.com/" + random.choice(sections)
        
        if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
            return "Ooppsss..., the link you gave is wrong...\nor down I guess?", 0
            
        else:
            page = requests.get(link)
            soup = bs(page.content, "html.parser")
            topics = (soup.find_all("h3", class_="article-name"))

            topic = str(random.choice(topics))[25:-5]
            for x in range(100):
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
        
        return f"{str(page_py.summary)}", f"Full URL = {page_py.fullurl}\nCanonical URL = {page_py.canonicalurl}"

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

def bio_abs(link):
    
    if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
        return "Ooppsss..., the link you gave is wrong...\nor down I guess?", 0
        
    else:
        page = requests.get(link)
        soup = bs(page.content, "html.parser")
        results = (soup.find_all("div", id="enc-abstract"))

        for x in results:
            abio = x.find('p').get_text().rstrip()

        return abio, link
     
def assess(message):
    
    with open("params.json") as data:
        ref = json.load(data)

    allow = False
    for x in ref["thank_you"]:
        if re.match(f"^{x[:round(len(x)/2)]}.*", message, re.IGNORECASE):
            return 1
        else:
            allow = True
            
    if allow is True:
        reff = message.split(' ')
        
        if len(message.split(' ')) > len(ref["thank_you"]):
            for x in ref["thank_you"]:
                for i in range(len(reff)):
                    if reff[i:i+len(x.split(' '))] == x.split(' '):
                        return 0
                    else:
                        return False
                
        elif len(ref["thank_you"]) > len(message.split(' ')):
            for i in range(len(reff)):
                for x in ref["thank_you"]:
                    if reff[i:i+len(x.split(' '))] == x.split(' '):
                        return 0
                    else:
                        return False
                
                        
