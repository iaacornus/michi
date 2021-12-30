import wikipediaapi
import re
import requests
from bs4 import BeautifulSoup as bs
import urllib.request
from difflib import SequenceMatcher

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
    defi = page_py.summary
    
  else:
    if (define[0].upper()+define[1].lower()) not in comb:
      pass
    else:
      wiki = "https://en.wikipedia.org/wiki/Special:AllPages/" + define[0].upper() + define[1].lower()

      page = requests.get(wiki)

      if urllib.request.urlopen(wiki).getcode() not in [x for x in range(200, 299)]:
        pass
        #await message.channel.send(f"{message.author.mention} the source is unfortunately down ...")
      else:
        soup = bs(page.content, "html.parser")
        topics = soup.find_all("a", class_="mw-redirect")

      dic = {}
      for x in topics:
        dic[SequenceMatcher(None, x.get_text(), define).ratio()] = x.get_text()
      
      hi = max(dic, key=dic.get)
      defi = f"Maybe you mean {dic[hi]}?"
  
  return defi
