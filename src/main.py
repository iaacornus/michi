import os
import discord
from discord import user
from dotenv import load_dotenv
from discord.ext import commands

from bs4 import BeautifulSoup as bs
import urllib.request
import random
import requests

from func import get_defin

load_dotenv()

TOKEN = #<TOKEN> os.getenv("DISCORD_TOKEN")
my_id = <ID>
#guild_ids = <GUILD_ID> #os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix="--")
client = discord.Client()

interesting = ["physics", "science", "chemistry", "multiverse", "time", "travel", "wormholes", "biology", "do you know", "know", "what", "interesting", "iaacornus", "cell", "culture", "virus", "molecule", "chem", "bio", "thermodynamics"]

print("STARTING BOT")


@client.event
async def on_ready():
  print("[BOT ONLINE]")

@client.event
async def on_message(message):
  
  if message.author == client.user:
    return

  for x in interesting:
    if x in message.content.lower():
      await message.channel.send(f"<@{my_id}> there's something interesting...")
      
  if message.content.lower() == "--topic":
    sections = ["space", "health", "planet-earth", "strange-news", "animals", "history"]
    link = "https://www.livescience.com/" + random.choice(sections)
    print(link)
    page = requests.get(link)

    if urllib.request.urlopen(link).getcode() not in [x for x in range(200, 299)]:
      pass
      #await message.channel.send(f"{message.author.mention} the source is unfortunately down ...")
    else:
      soup = bs(page.content, "html.parser")
      topics = (soup.find_all("h3", class_="article-name"))

    topic = str(random.choice(topics))[25:-5]
    for x in range(10):
      if ("top" or str(x) or "top " + str(x)) in str(topic):
        pass
      else :
        dec = topic
    await message.channel.send(f"<@{message.author.id}> {dec}")


@client.command()
async def get_def(ctx, word):
  await ctx.channel.send(get_defin(word))

client.run(TOKEN)
