# Docs

This documentations is for developers as there are no documentations in the source code.

# Functions

- [X] **--define**

This function defines a given word/phrase using the summary from [wikipedia](https://www.wikipedia.org/). 

This uses `wikipedia-api` from PyPI repo. First is it checks the availability of the page, if the page exists on wikipedia, if `True` it returns the `url` and `defi` (definition : `str`) variable :

    
    if page_py.exists() is True:
        defi = f"{str(page_py.summary)}"
        url = f"Full URL = {page_py.fullurl}\nCanonical URL = {page_py.canonicalurl}"
       
else, it would either give a suggestion for the `arg` (argument : str), _IF_ wikipidea is online _AND IF_ `(define[0].upper()+define[1].lower())` is in combination of first letters of the argument of wikipidea (Aa, Ab, Ac,... Zz). However if wikipidea returns a status code outside of range of successful status code (e.g. 200) it would `return "the source is unfortunately down ...", 0`, if it is online but the word is not in combination of letters, it would `return "the given term is not in Wikipedia, kindly correct the term and try again.", 0`
      
- [X] **--topic**

This function gives a topic from the science news for the week reported by [LiveScience](https://www.livescience.com/) it randomly selects on sub-sections of : `["space", "health", "planet-earth", "strange-news", "animals", "history"]` and picks a random news from the selected section.

_**On development functions**_

- [X] **Scam links removal (automatic)**

This is rather a filter than a function. This works by scanning all the messages of the user, if the message contain a spam link, it would be removed while pinging the staff at the same time. But, depending on the permissions of the bot, if the bot is allowed to manage the server it would instead kick/ban the member instead of pinging the staff.

The bot base its judgment from the parameters in [`params.py`](https://github.com/yaacornus/cornusbot/blob/devel/src/func.py). Using `SequenceMatcher` from `difflib`, it ratios the difference from all of references and the message sent by user, if the percent similarity is greater than 35%, it removes the messages and pings the user to give a reminder of no scam links, or it can be configured to make its own judgment (e.g. kick or ban the message author).

    for x, z in zip(scam().scams, scam().scam_link):
      if (SequenceMatcher(None, message.content.lower(), x).ratio() > 0.35) or SequenceMatcher(None, message.content.lower(), z).ratio() > 0.35:
          await message.delete()
          await message.channel.send(f"<@{message.author.id}> no scam links ...")
          break


- [ ] **No homework dump message/reminder (automatic)**

There are science servers where homework dumps are not allowed, however there are still members that joins with an aiming of being spoonfed with the answers. This works by asking every new members if they are on the particular server for homework or not, _Are you here for homework_ or depending on the host, depending on the response the bot would determine whether to welcome the member or remind them of rules, and in persistence they would be kicked.

# Functions to be added

- [X] Topic
- [X] Define
- [ ] Scam links removal
- [ ] No homework dump message/reminder
- [ ] Scientific paper abstract return
- [ ] Scientific calculation
- [ ] Simple science questions answer
