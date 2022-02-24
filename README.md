# Michi

Mainly for Science servers. It is composed of various functions that would be beneficial for members.

# Functions

Since comit `817482d83b8ee8e333e68bca5394b4f4d56468e4`, the bot used `~` as command prefix instead of `--`, mainly for easier use.

- [X] **Define word/phrase, `~define <word/phrase>, aliases=["def", "whatis"]`**

This defines a given word/phrase using the summary from [wikipedia](https://www.wikipedia.org/). This returns the definition of the word, if the page does exists, else depending on the case it would return a certain response.

Firstly, it would manually check if the word is in wikipedia, if it is not in dictionary it would return _"the given term is not in Wikipedia, kindly correct the term and try again."_ and if it is in dictionary it would return a word suggest given by `pyenchant`

- [X] **Give interesting science topic, `~topic, aliases=["anything-interesting"]`**

This function gives a topic from the science news for the week reported by [LiveScience](https://www.livescience.com/) it randomly selects on sub-sections of : `["space", "health", "planet-earth", "strange-news", "animals", "history"]` and picks a random news from the selected section.

- [X] **Scam links removal (automatic)**

This works by scanning all the messages of the user, if the message contain a spam link, it would be removed while pinging the staff at the same time. But, depending on the permissions of the bot, if the bot is allowed to manage the server it would instead kick/ban the member instead of pinging the staff.

The messages were referenced to repository of ~10000 discord phishing links provided by [Chillihero's](https://github.com/nikolaischunk) _et al._ [discord and suspicious links repository]https://github.com/nikolaischunk/discord-phishing-links). If it is not matched, its percent similarity were taken for further evaluation, and if it matched with at least 85%, the message will be removed.

- [X] **Thank you card feature (automatic)**

Just to lighten the mood! This works by analyzing the message of the user, if the bot determined that it is saying thank you to particular person, it would emphasize it by giving it a reward like virtual object, which is _thank you card_.

- [X] **Scientific paper abstract return (_currently only works with PubMed_), `~abs-bio <PubMed link>`**

This returns the abstract of a given PubMed paper link, including the given URL.

- [X] **OH is HYDROXIDE 🧪**

This just sends HYDROXIDE 🧪 everything a `message.content.lower()` is "OH" or "oh".

_Credits to BioBoat_

- [X] **Greet/reply to greetings**

The bot would reply to greetings made by the members with the references given in [params.py](https://github.com/yaacornus/cornusbot/blob/devel/src/params.json), with emoticons.

- [X] **Source code send, `~src-code`**

This sends the source code repository of the bot for whoever who requested or issued the command, whatever the purpose is. Then the bot deletes the message of the author immediately after recognition followed by the deletion of its response (the source code with some response) after 60.0 seconds.

# On development functions

- [ ] **No homework dump message/reminder (automatic)**

There are science servers where homework dumps are not allowed, however there are still members that joins with an aiming of being spoonfed with the answers. This works by asking every new members if they are on the particular server for homework or not, _Are you here for homework_ or depending on the host, depending on the response the bot would determine whether to welcome the member or remind them of rules, and in persistence they would be kicked.

- [ ] **Simple science questions answer**

Science servers are often thought as answer source, commonly bastard users dump trivial or even simple uninteresting questions to whatever science server they find. This works by fetching the question from the user and returning the answer taken from Google, it is also planned to put a repository for question and answers to be able to give more reliable answer than something given by Google scraped by bot without further review.

# Setup for own hosting

The requirements of the bots are listed in `requirements.txt` and can be installed with

    pip install -r requirements.txt
    
Then using git clone, the main branch (stable) repository can be cloned :

    git clone https://github.com/yaacornus/cornusbot
    
However, the stable branch can be short on features. Unstable or [`devel`](https://github.com/yaacornus/cornusbot/tree/devel) branch can be cloned to accessa feature rich version, this is not as unstable as thought, and this has undergone preliminary testing before having the code commited.

    git clone --branch devel https://github.com/yaacornus/cornusbot

# Invite

The bot is currently in development phase, the link would be posted as soon as it enters the stable version.

# Functions to be added

- [X] Topic
- [X] Define
- [X] Scam links removal
- [ ] No homework dump message/reminder
- [X] Scientific paper abstract return
- [ ] Scientific calculation
- [ ] Simple science questions answer
- [X] Greet

# Contribution

For contribution, just make a pull request and the code changes would be reviewed for merging with the branch.

Join the [discord server](https://discord.gg/auArnV8Yz2) for testing ! :

https://discord.gg/auArnV8Yz2

# Credits

Credits to [Chillihero's](https://github.com/nikolaischunk) _et al._ [discord and suspicious links repository]https://github.com/nikolaischunk/discord-phishing-links).
