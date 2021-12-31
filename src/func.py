import wikipediaapi
import urllib.request
import enchant

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
              
