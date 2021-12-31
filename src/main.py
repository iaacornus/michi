import discord
from discord import user
from discord import message
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands

from func import get_defin, give_topic
from params import interesting, scam

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

    ratio = []
    for x in interesting().interesting:
        for y in message.content.lower().split(' '):  
            ratio.append(SequenceMatcher(None, y, x).ratio())

    if max(ratio) > 0.75:
        await message.channel.send(f"<@{my_id}> there's something interesting...")   
     
    for x, z in zip(scam().scams, scam().scam_link):
        if (SequenceMatcher(None, message.content.lower(), x).ratio() > 0.35) or SequenceMatcher(None, message.content.lower(), z).ratio() > 0.35:
            await message.delete()
            await message.channel.send(f"<@{message.author.id}> no scam links ...")
            break

    await client.process_commands(message)


@client.command(name="topic")
async def topic(ctx):
    dec = give_topic()
    
    if dec is False:
        await ctx.channel.send(f"<@{ctx.author.id}> the source is unfortunately down ...")
    else:
        await ctx.channel.send(f"<@{ctx.author.id}> {dec}")

@client.command(name="define")
async def wiki(ctx, word):
    mess, url = get_defin(word)

    if len(mess) > 1800:
        wc = len(mess) ; delimiter = 1800 ; start = 0
        stop = False

        while stop is False:
            
            if wc > 1800 :
                if start == 0:
                    await ctx.channel.send(f"<@{ctx.author.id}> {str(mess)[start:delimiter]}-")
                else:
                    await ctx.channel.send(f"-{str(mess)[start:delimiter]}-")
                
                start += 1800 ; delimiter += 1800 ; wc -= 1800      
                
            elif wc < 1800:
                await ctx.channel.send(f"-{str(mess)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                stop = True

    else:
        if url == 0:
            await ctx.channel.send(f"<@{ctx.author.id}> {mess}")
        else:
            await ctx.channel.send(f"<@{ctx.author.id}> {mess}")
            await ctx.channel.send(url)


client.run(TOKEN)

