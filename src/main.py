import discord
from discord import user
from discord import message
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands

from func import get_defin, give_topic, bio_abs
from params import params

import re
from difflib import SequenceMatcher

load_dotenv()

"""REPLACE THESE"""
TOKEN = #<TOKEN> os.getenv("DISCORD_TOKEN")
my_id = #<ID>
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

    for x in params().scams:
        if SequenceMatcher(None, message.content.lower(), x.lower()).ratio() > 0.65:
            await message.delete()
            await message.channel.send(f"<@{message.author.id}> no scam links ...")
            break
    
    
    for x in params().thank_message:
        if re.match(f"^{x[:round(len(x)/2)]}.*", message.content.lower(), re.IGNORECASE):
            await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!!")    
            break
    
    await client.process_commands(message)


@client.command(name="topic")
async def topic(ctx):
    dec = give_topic()

    await ctx.channel.send(f"<@{ctx.author.id}> the source is unfortunately down ...") if dec is False else await ctx.channel.send(f"<@{ctx.author.id}> {dec}")

@client.command(name="define")
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
     
     
@client.command(name="abs-bio")
async def absBio(ctx, link):
    absBio, url = bio_abs(link)

    await ctx.channel.send(f"<@{ctx.author.id}> {absBio}") if url == 0 else await ctx.channel.send(f"<@{ctx.author.id}> {absBio}\n{url}")
     
    
     

client.run(TOKEN)

