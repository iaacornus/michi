import discord
from discord import user
from discord import message
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands

from func import get_defin, give_topic, bio_abs, assess

from difflib import SequenceMatcher

import json

load_dotenv()

"""REPLACE THESE"""
TOKEN = #<TOKEN> os.getenv("DISCORD_TOKEN")
#guild_ids = <GUILD_ID> #os.getenv("DISCORD_GUILD")

client = commands.Bot(command_prefix="--")

print("STARTING BOT")

@client.event
async def on_ready():
    print("[BOT ONLINE]")

@client.event
async def on_message(message):
  
    if message.author == client.user:
        return

    with open("params.json") as data:
        ref = json.load(data)
        
    # scam filter
    ratio = []
    for x in ref["scams"]:
        ratio.append(SequenceMatcher(None, x.lower(), message.content.lower()).ratio())
        
    if (sum(ratio)/(len(ref["scams"])) > 0.2) and (max(ratio) > 0.85):    
        await message.delete()
        await message.channel.send(f"<@{message.author.id}> no scam links ...")
        
    # thank you card
    thank_ratio = []
    mess_as = assess(message.content.lower())
    if mess_as == 1:
        await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!!")
        
    
    elif mess_as == 0:
            
        for y in ref["thank_message"]:
            thank_ratio.append(SequenceMatcher(None, y.lower(), message.content.lower()).ratio())
                                    
        if (sum(thank_ratio)/(len(ref["thank_message"])) > 0.2) and (max(thank_ratio) > 0.85):      
            await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!!")    
                
                
    # hydroxide!
    if message.content.lower() == "oh":
        await message.channel.send("HYDROXIDE :test_tube:")
            
    await client.process_commands(message)


@client.command(name="topic", help="This function gives a topic from the science news for the week reported by LiveScience.")
async def topic(ctx):
    dec = give_topic()

    await ctx.channel.send(f"<@{ctx.author.id}> the source is unfortunately down ...") if dec is False else await ctx.channel.send(f"<@{ctx.author.id}> {dec}")


@client.command(name="define", help="This defines a given word/phrase using the summary from wikipedia.")
async def wiki(ctx, word):
    mess, url = get_defin(word)

    if len(mess) > 1800:
        wc = len(mess) ; delimiter = 1800 ; start = 0
        stop = False

        while stop is False:
            
            if wc > 1800 :
                await ctx.channel.send(f"<@{ctx.author.id}> {str(mess)[start:delimiter]}-") if start == 0 else await ctx.channel.send(f"-{str(mess)[start:delimiter]}-")
                start += 1800 ; delimiter += 1800 ; wc -= 1800      
                
            elif wc < 1800:
                await ctx.channel.send(f"-{str(mess)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                stop = True

    else:
        await ctx.channel.send(f"<@{ctx.author.id}> {mess}") if url == 0 else await ctx.channel.send(f"<@{ctx.author.id}> {mess}\n{url}")
     
     
@client.command(name="abs-bio", help="This returns the abstract of a given PubMed link.")
async def absBio(ctx, link):
    absBio, url = bio_abs(link)
    
    if len(absBio) > 1800:
        wc = len(absBio) ; delimiter = 1800 ; start = 0
        stop = False

        while stop is False:
            
            if wc > 1800 :
                await ctx.channel.send(f"<@{ctx.author.id}> {str(absBio)[start:delimiter]}-") if start == 0 else await ctx.channel.send(f"-{str(absBio)[start:delimiter]}-")
                start += 1800 ; delimiter += 1800 ; wc -= 1800      
                
            elif wc < 1800:
                await ctx.channel.send(f"-{str(absBio)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                stop = True

    else:
        await ctx.channel.send(f"<@{ctx.author.id}> {absBio}") if url == 0 else await ctx.channel.send(f"<@{ctx.author.id}> {absBio}\n{url}")     
        
    
client.run(TOKEN)

