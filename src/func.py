import os
from turtle import color
from typing import final
import wikipediaapi
import urllib.request
import enchant

from bs4 import BeautifulSoup as bs
from difflib import SequenceMatcher as SM

import requests
import random
import json
import re
import os

from colors import COLORS

color = COLORS

class database:
    with open("./database/params.json") as data:
        ref = json.load(data)

    with open("./database/suspicious-links.json") as data1:
        ref1 = json.load(data1)

    with open("./database/discord-links.json") as data:
        ref2 = json.load(data)

    
class functions:
    def __init__(self) -> None:
        pass
                
    def give_topic(ref=database.ref) -> str:
        
        while True:
            sections = ["space", "health", "planet-earth", "strange-news", "animals", "history"]
            link = "https://www.livescience.com/" + random.choice(sections)
            
            if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
                return f"Ooppsss..., the link you gave :  _{link}_ is wrong {random.choice(ref['sad'])}...\nor down I guess??? {random.choice(ref['confused'])}", 0
                
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
        

    def get_defin(define, ref=database.ref) -> str:
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
                return f"uhmm..., sorry the term '{define}' is not in Wikipedia.\nPlease kindly correct the term and try again ...", 0
            else:
                wiki = "https://en.wikipedia.org/wiki/Special:AllPages/" + define[0].upper() + define[1].lower()
                
                if urllib.request.urlopen(wiki).getcode() not in [x for x in range(200, 299)]:
                    return f"the source is unfortunately down ... {random.choice(ref['sad'])}", 0
                else:
                    lang = enchant.Dict("en_US")
                    lang.check(define)

                    return f"um... maybe you mean {str(lang.suggest(define)).replace('[', '').replace(']', '')}???? {random.choice(ref['confused'])}", 0

    def bio_abs(link, ref=database.ref) -> str:
            
        if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
            return f"Ooppsss..., the link you gave is wrong {random.choice(ref['sad'])}...\nor down I guess? {random.choice(ref['confused'])}", 0
            
        else:
            page = requests.get(link)
            soup = bs(page.content, "html.parser")
            results = (soup.find_all("div", id="enc-abstract"))

            for x in results:
                abio = x.find('p').get_text().rstrip()

            return abio, link
        
    def thank_youCard(message, ref=database.ref) -> bool:
        reff = [x for x in message.lower().split(' ') if not re.match(f"^<@.*", x, re.IGNORECASE)]
        
        for x in ref["thank_you"]:
            if (re.match(f"^{x[:round(len(x)/2)]}.*", ' '.join([x for x in reff]), re.IGNORECASE)) or (re.match(f"^{x[:round(len(x)/2)]}.*", message, re.IGNORECASE)) or (set(x.split(' ')) == set(reff)):
                return True
            else:
                if x in message.lower():
                    return False
                else:
                    continue   
                            
    def filter(message, ref1=database.ref1, ref2=database.ref2) -> bool:
        mess_content = message.split(' ')
        print(mess_content)
                
        for x in mess_content:
            if (x.lower().replace(' ','') in ref1) or (x.lower().replace(' ','') in ref2) or SM(None, x.lower(), ).ratio():
                return True
            else:
                return False
