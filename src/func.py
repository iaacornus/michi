from random import choice as ch
import re
import urllib.request
from difflib import SequenceMatcher as SM

import wikipediaapi
import enchant
import requests
from bs4 import BeautifulSoup as bs

from colors import COLORS

color = COLORS


class functions:
    def __init__(self) -> None:
        pass

    def give_topic(self) -> str:
        while True:
            sections = [
                "space",
                "health",
                "planet-earth",
                "strange-news",
                "animals",
                "history"
            ]
            link = "https://www.livescience.com/" + ch(sections)

            if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
                return (
                    f"Ooppsss..., the link you gave :  _{link}_ is wrong {ch(self.ref['sad'])}...\nor down I guess??? {ch(self.ref['confused'])}",
                    False)

            else:
                page = requests.get(link)
                soup = bs(page.content, "html.parser")
                topics = (soup.find_all("h3", class_="article-name"))

                topic = str(ch(topics))[25:-5]
                for i in range(100):
                    if ("top" or str(i) or f"top {i}" or "best") in str(topic):
                        continue
                    else:
                        return topic

    def get_defin(self, define) -> str:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(define)

        alpha = list("abcdefghijklmnopqrstuvwxyz")
        ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        comb = []
        for x in ALPHA:
            for y in alpha:
                comb.append(x+y)

        if page_py.exists():
            return (
                f"{str(page_py.summary)}",
                f"Full URL = {page_py.fullurl}",
                f"Canonical URL = {page_py.canonicalurl}"
            )

        else:
            lang = enchant.Dict("en_US")
            lang.check(define)
            suggestion = str(lang.suggest(define))[1:-1]

            return (
                f"um... maybe you mean {suggestion}???? {ch(self.ref['confused'])}",
                False
            )

    def bio_abs(self, link) -> str:
        if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
            return (
                f"Ooppsss..., the link you gave is wrong {ch(self.ref['sad'])}...\nor down I guess? {ch(ref['confused'])}",
                False
            )

        else:
            page = requests.get(link)
            soup = bs(page.content, "html.parser")
            results = (soup.find_all("div", id="enc-abstract"))

            for item in results:
                abstract = item.find("p").get_text().rstrip()

            return abstract, link

    def thank_you_card(self, message, ref) -> bool:
        word_ref = [word for word in message.lower().split(" ") if not re.match(f"^<@.*", word, re.IGNORECASE)]

        for ref_ty in ref["thank_you"]:
            pattern = f"^{ref_ty[:round(len(ref_ty)/2)]}.*"
            evaluate_1 = re.match(pattern, " ".join([word for word in word_ref]), re.IGNORECASE)
            evaluate_2 = re.match(pattern, message, re.IGNORECASE)

            if set(ref_ty.split(" ")) == set(word_ref) or evaluate_1 or evaluate_2:
                return True
            else:
                if ref_ty in message:
                    return False
                else:
                    continue

    def filter(self, message) -> bool:
        msg_content = message.lower().split(" ").replace(" ","")

        for words in msg_content:
            if (words in self.ref1) or (words in self.ref2):
                return True
            else:
                return False
