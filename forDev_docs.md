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

- [X] **Scam links removal (automatic)**

This is rather a filter than a function. This works by scanning all the messages of the user, if the message contain a spam link, it would be removed while pinging the staff at the same time. But, depending on the permissions of the bot, if the bot is allowed to manage the server it can be modified to instead kick/ban the member instead of pinging the staff.

The bot base its judgment from the parameters in [`params.json`](https://github.com/yaacornus/cornusbot/blob/devel/src/params.json). Using `SequenceMatcher` from `difflib`, it ratios the difference from all of references and the message sent by user, if the average percent similarity is greater than 20% and the statement percent similarity is greater than 80%, it removes the messages and pings the user to give a reminder of no scam links, or it can be configured to make its own judgment (e.g. kick or ban the message author).
       
    # scam filter
    ratio = []
    for x in ref["scams"]:
        ratio.append(SequenceMatcher(None, x.lower(), message.content.lower()).ratio())
        
    if (sum(ratio)/(len(ref["scams"])) > 0.2) and (max(ratio) > 0.85):    
        await message.delete()
        await message.channel.send(f"<@{message.author.id}> no scam links ...")

- [X] **Thank you card feature (automatic)**

This works by analyzing the message of the user, if the bot determined that it is saying thank you to particular person, it would emphasize it by giving it a reward like virtual object, which is _thank you card_.

It has also the same judgment with scam links removal, with its own references of `thank_you` words/phrases and `thank_message` (thank you messages) in [`params.json`](https://github.com/yaacornus/cornusbot/blob/devel/src/params.json). And to further assess the message, it utilizes `assess(message)` function in [`func.py`](https://github.com/yaacornus/cornusbot/blob/devel/src/func.py) which determines whether the message is a thank you message or a message that happens to just contain a word "thank you" or whatever "thank you" word in whatever language. This uses RegEx, if the word starts with a particular pattern and matches with the message : `re.match(f"^{x[:round(len(x)/2)]}.*", message, re.IGNORECASE)` it would be immediately considered a thank you. Else, it would further assess the message, using `if reff[i:i+len(x.split(' '))] == x.split(' ')` to know if it is a message that contains a thank you word and then passing it to `SequenceMatcher(x,y,z)`. If the average percent similarity is greater than 20% and the statement percent similarity is greater than 80%, it considers it a thank you message and sends a _thank you card_.

- [ ] **No homework dump message/reminder (automatic)**

There are science servers where homework dumps are not allowed, however there are still members that joins with an aiming of being spoonfed with the answers. This works by asking every new members if they are on the particular server for homework or not, _Are you here for homework_ or depending on the host, depending on the response the bot would determine whether to welcome the member or remind them of rules, and in persistence they would be kicked.

# Functions to be added

- [X] Topic
- [X] Define
- [X] Scam links removal
- [ ] No homework dump message/reminder
- [X] Scientific paper abstract return
- [ ] Scientific calculation
- [ ] Simple science questions answer
