# cornusbot

The main purpose of this bot is for benefit of the author, yaacornus/iaacornus, but it can still be used and serve with significant help particular for Science servers. It is composed of various functions that would be beneficial for members.

# Functions

- [X] **--define**

This defines a given word/phrase using the summary from [wikipedia](https://www.wikipedia.org/). This returns the definition of the word, if the page does exists, else depending on the case it would return a certain response.

  firstly, it would manually check if the word is in wikipedia, if it is not in dictionary it would return _"the given term is not in Wikipedia, kindly correct the term and try again."_ and if it is in dictionary it would return a word suggest given by `pyenchant`

- [X] **--topic**

This function gives a topic from the science news for the week reported by [LiveScience](https://www.livescience.com/) it randomly selects on sub-sections of : `["space", "health", "planet-earth", "strange-news", "animals", "history"]` and picks a random news from the selected section.

_**On development functions**_

- [ ] **Scam links removal (automatic)**

This works by scanning all the messages of the user, if the message contain a spam link, it would be removed while pinging the staff at the same time. But, depending on the permissions of the bot, if the bot is allowed to manage the server it would instead kick/ban the member instead of pinging the staff.

- [ ] **No homework dump message/reminder (automatic)**

There are science servers where homework dumps are not allowed, however there are still members that joins with an aiming of being spoonfed with the answers. This works by asking every new members if they are on the particular server for homework or not, _Are you here for homework_ or depending on the host, depending on the response the bot would determine whether to welcome the member or remind them of rules, and in persistence they would be kicked.

# Setup for own hosting

The requirements of the bots are listed in `requirements.txt` and can be installed with

    pip install -r requirements.txt

# Invite

The bot is currently in development phase, the link would be posted as soon as it enters the stable version.

# Functions to be added

- [X] Topic
- [X] Define
- [ ] Scam links removal
- [ ] No homework dump message/reminder
- [ ] Scientific paper abstract return
- [ ] Scientific calculation
- [ ] Simple science questions answer

# Contribution

For contribution, just make a pull request and the code changes would be reviewed for merging with the branch.

Join the [discord server](https://discord.gg/auArnV8Yz2) for testing ! :

https://discord.gg/auArnV8Yz2
