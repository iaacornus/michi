import discord
from discord import user
from discord import message
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands

from func import get_defin, give_topic

load_dotenv()

"""REPLACE THESE"""
TOKEN = #<TOKEN> os.getenv("DISCORD_TOKEN")
my_id = #<ID>
#guild_ids = <GUILD_ID> #os.getenv("DISCORD_GUILD")

client = commands.Bot(command_prefix="--")

interesting = ["physics", "science", "chemistry", "multiverse", "time", "travel", "wormholes", "biology", "do you know",
               "know", "what", "interesting", "iaacornus", "cell", "culture", "virus", "molecule", "chem", "bio", "thermodynamics"]

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
            
    await client.process_commands(message)

@client.command(name="topic")
async def topic(ctx):
    dec = give_topic()
    
    if dec is False:
        await ctx.channel.send(f"<@{message.author.id}> the source is unfortunately down ...")
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

