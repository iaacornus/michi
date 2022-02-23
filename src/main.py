import discord
from discord import user
from discord.errors import ClientException
from dotenv import load_dotenv
from discord.ext import commands
from matplotlib import colors

from func import functions, database
from colors import COLORS

from difflib import SequenceMatcher as SM
import random
import os

load_dotenv()

"""REPLACE THESE"""
TOKEN = "OTI2MDQ1OTA0NTIyMzM4MzE0.Yc19dA.d8oVzCUjoONs7gEVJY2t2Awe-Lw"
#guild_ids = <GUILD_ID> #os.getenv("DISCORD_GUILD")

# preparation, this is where the bot update the database for phishing links,
#and this is where the bot itself starts and prepares the necessary for function

function = functions
color = COLORS()

if __name__ == "__main__":
    pass

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
    if input("Everything ready, clear the system? [y/N]").lower().replace(' ', '') == 'y':
        os.system("clear")
    print(color.GREEN + "[BOT STARTED]" + color.END)


@client.event
async def on_message(message, ref=database.ref, ref1=database.ref1, ref2=database.ref2):
      
    # preload
    if message.author == client.user:
        return


    # delete --abs-bio and --source-code command
    if (("~abs-bio" and "https://") in message.content.lower()) or (message.content.lower() == "~source-code"):
        await message.delete()
        
    # hydroxide!s
    elif message.content.lower() == "oh":
        await message.channel.send(f"HYDROXIDE :test_tube:\nA fuel yayyy! {random.choice(ref['happy'])}")


    # scam filter 
    mess_indv = message.content.lower().split(' ')
    
    for sample in mess_indv:    
        if function.filter(sample) is True:
            await message.delete()
            await message.channel.send(f"<@{message.author.id}> {random.choice(ref['for_scam'])} {random.choice(ref['angry'])}...")
        
        # re-run the message by getting the percent different from the messages into the scam links
        # with in the database, and if it is greater than 85%, delete the message and warn user
        else:
            ratio = [SM(None, x.lower(), sample).ratio()
                    for x in ref1["domains"]] + [SM(None, y.lower(), sample).ratio()
                                            for y in ref2["domains"]] + [SM(None, z.lower(), sample).ratio()
                                                                         for z in ref["scams"]] 
                                                     
            if max(ratio) > 0.85:    
                await message.delete()
                await message.channel.send(f"<@{message.author.id}> {random.choice(ref['for_scam'])} {random.choice(ref['angry'])}...")
            else:
                continue   
             
        break
    

    # thank you card
    mess_as = function.thank_youCard(message.content.lower())   
    if mess_as is True:
        await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!! {random.choice(ref['happy'])}")
        
    elif mess_as is False:        
        if max([SM(None, x.lower(), message.content.lower()).ratio() for x in ref["thank_message"]]) > 0.75:
            await message.channel.send(f"<@{message.author.id}> gave you a _thank you_ card!! {random.choice(ref['happy'])}")    
    

    # greet the person
    if max([SM(None, x.lower(), message.content.lower()).ratio() for x in ref["greetings"]]) > 0.8:
        mess = random.choice(ref["greetings"])
        
        if random.choice([True, False]) is True:
            await message.channel.send(f"{mess}{''.join(['~' for x in range(random.randint(1,3))])} <@{message.author.id}>! {random.choice(ref['greet'])}")
        else:
            await message.channel.send(f"{mess} <@{message.author.id}>! {random.choice(ref['greet'])}")

    
    """ this ping response, maybe too long and complex or complicated, however it was
    designed to be able to display some sort of pseudoemotions, or reaction from the bot""" 
    # ping response
    if f"<@!{message.author.id}>" == f"<@!919442885248692235>":
        await message.channel.send(f"Hey boss! {random.choice(ref['happy'])}")                    
   
    elif f"<@!{client.user.id}>" == message.content.lower():
        choice = random.choice([True, False])

        # neutral response
        if choice is True:
            await message.channel.send(f"{random.choice(ref['ping_res'])} <@{message.author.id}>?")
        # pissed off
        else:
            await message.channel.send(f"{random.choice(ref['angry_res'])} <@{message.author.id}> {random.choice(ref['angry'])}.")
        
    # happy or respectful response
    elif max([SM(None, f"{x} <@!{client.user.id}>", message.content.lower()).ratio() for x in ref["greetings"]]) > 0.8:
        await message.channel.send(f"{random.choice(ref['greetings'])}{''.join(['~' for x in range(random.randint(1,3))])} <@{message.author.id}>! {random.choice(ref['greet']) if random.choice([True, False]) is True else random.choice(ref['happy'])}") 

            
    # process the commands
    await client.process_commands(message)


@client.command(name="topic", aliases=["anything-interesting"],
                help="This function gives a topic from the science news for the week reported by LiveScience.")
async def topic(ctx, ref=database.ref):
    dec = function.give_topic()
            
    await ctx.reply(f"sorry, the source is unfortunately down, please try again later... {random.choice(ref['sad'])}", mention_author=True) if dec is False else await ctx.reply(f"{dec} {random.choice(ref['surprised'])}", mention_author=True)



@client.command(name="define", aliases=["whatis", "def"],
                help="This defines a given word/phrase using the summary from wikipedia.")
async def wiki(ctx, word, ref=database.ref):
    mess, url = function.get_defin(word)
    
    if len(mess) > 1500:
        wc = len(mess) ; delimiter = 1500 ; start = 0

        while True:
            
            if wc > 1500 :
                await ctx.reply(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{str(mess)[start:delimiter]}-", mention_author=True) if start == 0 else await ctx.channel.send(f"-{str(mess)[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500      
                
            elif wc < 1500:
                await ctx.channel.send(f"-{str(mess)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                break
    else:
        await ctx.reply(mess, mention_author=True) if url == 0 else await ctx.reply(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{mess}\n{url}", mention_author=True)
     
     
     
@client.command(name="abs-bio", aliases=["fetch", "paper"],
                help="This returns the abstract of a given PubMed link.")
async def absBio(ctx, link, ref=database.ref):
    absBio, url = function.bio_abs(link)
         
    if len(absBio) > 1500:
        wc = len(absBio) ; delimiter = 1500 ; start = 0

        while True:
            
            if wc > 1500 :
                await ctx.channel.send(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{str(absBio)[start:delimiter]}-") if start == 0 else await ctx.channel.send(f"-{str(absBio)[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500      
                
            elif wc < 1500:
                await ctx.channel.send(f"-{str(absBio)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                break
    else:
        await ctx.channel.send(f"<@{ctx.author.id}> {absBio}") if url == 0 else await ctx.channel.send(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\n{absBio}\n{url}")     
    
        
@client.command(name="src-code",
                help="Send the source code repository of the bot.")   
async def src_code(ctx, ref=database.ref):
    await ctx.channel.send(f"Here you go <@{ctx.author.id}>! {random.choice(ref['happy'])}\nhttps://github.com/iaacornus/cornusbot", delete_after=60.0)
            
 
client.run(TOKEN)

