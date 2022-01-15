import asyncio
import discord
from discord import user
from discord import message
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands

from func import get_defin, give_topic, bio_abs, assess

from difflib import SequenceMatcher

import random
import json
import re

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
      
    # preload
    if message.author == client.user:
        return

    # open references
    with open("params.json") as data:
        ref = json.load(data)
    
    
    # delete --abs-bio command
    if ("--abs-bio" and "https://") in message.content.lower():
        await message.delete()
    
    
    # scam filter
    ratio = []
    for x in ref["scams"]:
        ratio.append(SequenceMatcher(None, x.lower(), message.content.lower()).ratio())
        
    if (sum(ratio)/(len(ref["scams"])) > 0.2) and (max(ratio) > 0.65):    
        await message.delete()
        await message.channel.send(f"<@{message.author.id}> {random.choice(ref['for_scam'])} {random.choice(ref['angry'])}...")
        
        
    # thank you card
    mess_as = assess(message.content.lower())
    if mess_as == 1:
        await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!! {random.choice(ref['happy'])}")
        
    elif mess_as == 0:        
        thank_ratio = []
        
        for x in ref["thank_message"]:
            thank_ratio.append(SequenceMatcher(None, x.lower(), message.content.lower()).ratio())    
            
        if max(thank_ratio) > 0.75:      
            await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!! {random.choice(ref['happy'])}")    
    
    
    # greet the person
    greet_ref = [SequenceMatcher(None, x.lower(), message.content.lower()).ratio() for x in ref["greetings"]]
    if max(greet_ref) >= 0.8:
        mess = random.choice(ref["greetings"])
        #await message.channel.send(f"{mess} {''.join(["~" for x in random.randint(1,3)])} <@{message.author.id}>!") if
        # random.choice([True, False]) is True else message.channel.send(f"{mess} <@{message.author.id}>!")
        if random.choice([True, False]) is True :
            await message.channel.send(f"{mess}{''.join(['~' for x in range(random.randint(1,3))])} <@{message.author.id}>! {random.choice(ref['greet'])}")
        else:
            await message.channel.send(f"{mess} <@{message.author.id}>! {random.choice(ref['greet'])}")
        
    # ping response
    if f"<@!{client.user.id}>" in message.content.lower():
        choice = random.choice([1,2,3])
        # 1 is good mood
        if choice == 1:
            await message.channel.send(f"{random.choice(ref['greetings'])}{''.join(['~' for x in range(random.randint(1,3))])} <@{message.author.id}>! {random.choice(ref['greet']) if random.choice([True, False]) is True else random.choice(ref['happy'])}")
        # no idea
        elif choice == 2:
            await message.channel.send(f"{random.choice(ref['ping_res'])} <@{message.author.id}>?")
        # pissed off
        else:
            await message.channel.send(f"{random.choice(ref['angry_res'])} <@{message.author.id}> {random.choice(ref['angry'])}.")
        
                           
    # hydroxide!s
    if message.content.lower() == "oh":
        await message.channel.send(f"HYDROXIDE :test_tube:\nA fuel yayyy! {random.choice(ref['happy'])}")
    
            
            
    await client.process_commands(message)


@client.command(name="topic", help="This function gives a topic from the science news for the week reported by LiveScience.")
async def topic(ctx):
    dec = give_topic()
    
    with open("params.json") as data:
        ref = json.load(data)
        
    await ctx.reply(f"sorry, the source is unfortunately down, please try again later... {random.choice(ref['sad'])}", mention_author=True) if dec is False else await ctx.reply(f"{dec} {random.choice(ref['surprised'])}", mention_author=True)



@client.command(name="define", aliases=["whatis", "def"], help="This defines a given word/phrase using the summary from wikipedia.")
async def wiki(ctx, word):
    mess, url = get_defin(word)
    
    with open("params.json") as data:
        ref = json.load(data)
    

    if len(mess) > 1500:
        wc = len(mess) ; delimiter = 1500 ; start = 0
        stop = False

        while stop is False:
            
            if wc > 1500 :
                await ctx.reply(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{str(mess)[start:delimiter]}-", mention_author=True) if start == 0 else await ctx.channel.send(f"-{str(mess)[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500      
                
            elif wc < 1500:
                await ctx.channel.send(f"-{str(mess)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                stop = True

    else:
        await ctx.reply(mess, mention_author=True) if url == 0 else await ctx.reply(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{mess}\n{url}", mention_author=True)
     
     
     
@client.command(name="abs-bio", help="This returns the abstract of a given PubMed link.")
async def absBio(ctx, link):
    absBio, url = bio_abs(link)
  
    with open("params.json") as data:
        ref = json.load(data)
      
      
    if len(absBio) > 1500:
        wc = len(absBio) ; delimiter = 1500 ; start = 0
        stop = False

        while stop is False:
            
            if wc > 1500 :
                await ctx.channel.send(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{str(absBio)[start:delimiter]}-") if start == 0 else await ctx.channel.send(f"-{str(absBio)[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500      
                
            elif wc < 1500:
                await ctx.channel.send(f"-{str(absBio)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                stop = True

    else:
        await ctx.channel.send(f"<@{ctx.author.id}> {absBio}") if url == 0 else await ctx.channel.send(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{absBio}\n{url}")     
    
        
@client.command(name="source-code", help="Send the source code repository of the bot.")   
async def src_code(ctx):
    
    with open("params.json") as data:
        ref = json.load(data)

    await ctx.reply(f"Here you go {random.choice(ref['happy'])}\nhttps://github.com/yaacornus/cornusbot", mention_author=True, delete_after=60.0)
   
            
client.run(TOKEN)

