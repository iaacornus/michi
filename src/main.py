import discord
import os
import json
from random import choice as ch

from rich.console import Console
from func import functions
from dotenv import load_dotenv
from discord.ext import commands
from difflib import SequenceMatcher as SM


load_dotenv()

# TOKEN = # bot token
#guild_ids = <GUILD_ID> #os.getenv("DISCORD_GUILD")

if __name__ != "__main__":
    raise SystemExit("Exception raised.")

# ----------------------------------------------------------------
# load the data as well as other classes needed for use
# ----------------------------------------------------------------
function = functions()
console = Console()
client = commands.Bot(command_prefix="~")

with open("../database/params.json") as data:
    ref = json.load(data) # emotes, thank references, and greets

with open("../database/suspicious-links.json") as data1:
    ref1 = json.load(data1) # suspicious links lists

with open("../database/discord-links.json") as data:
    ref2 = json.load(data) # confirmed phishing links lists

# ----------------------------------------------------------------
@client.event
async def on_ready():
    if input("Everything ready, clear the system? [y/N]") == 'y':
        os.system("clear")
    console.log("[bold green]> BOT STARTED[/bold green]")


@client.event
async def on_message(message):
    msg = message.content.lower()
    mess_indv = msg.split(" ")
    msg_author = message.author.id

    if message.author == client.user:
        return

    # delete --abs-bio and --source-code command
    if (("~abs-bio" and "https://") in msg) or (msg == "~source-code"):
        await message.delete()
    elif msg == "oh": # hydroxide!s
        await message.channel.send(
            f"HYDROXIDE :test_tube:\nA fuel yayyy! {ch(ref['happy'])}"
        )

    # scam filter
    for words in mess_indv:
        if function.filter(words):
            await message.delete()
            await message.channel.send(
                f"<@{msg_author}> {ch(ref['for_scam'])} {ch(ref['angry'])}..."
            )
        else:
            ratio = (
                [SM(None, ref_dom, words).ratio() for ref_dom in ref1["domains"]]
                + [SM(None, ref_dom_2, words).ratio() for ref_dom_2 in ref2["domains"]]
                + [SM(None, ref_dom_3, words).ratio() for ref_dom_3 in ref["scams"]]
            )

            if max(ratio) > 0.85:
                await message.delete()
                await message.channel.send(
                    f"<@{msg_author}> {ch(ref['for_scam'])} {ch(ref['angry'])}..."
                )
            else:
                continue

        break

    if function.thank_you_card(msg, ref=ref):
        await message.channel.send(
            f"<@{msg_author}> gave you a _thank you_ card!! {ch(ref['happy'])}"
        )
    else:
        if max(
                [SM(None, ref_thank, msg).ratio() for ref_thank in ref["thank_message"]]
            ) > 0.75:
            await message.channel.send(
                f"<@{msg_author}> gave you a _thank you_ card!! {ch(ref['happy'])}"
            )

    # greeter
    if max([SM(None, ref_greet, msg).ratio() for ref_greet in ref["greetings"]]) > 0.8:
        greet_msg = ch(ref["greetings"])
        await message.channel.send(
            f"{greet_msg} <@{msg_author}>! {ch(ref['greet'])}"
        )
    elif max(
            [SM(None, f"{ref_greet} <@!{client.user.id}>", msg).ratio() for ref_greet in ref["greetings"]]
        ) > 0.8:
        emo_choice = ch(["greet", "happy"])
        await message.channel.send(
            f"{ch(ref['greetings'])} <@{msg_author}>! {ch(ref[{emo_choice}])}"
        )


    # ping response
    if f"<@!{msg_author}>" == f"<@!919442885248692235>":
        await message.channel.send(f"Hey boss! {ch(ref['happy'])}")
    elif f"<@!{client.user.id}>" == msg:
        if ch([True, False]): # neutral response
            await message.channel.send(
                f"{ch(ref['ping_res'])} <@{msg_author}>?"
            )
        else: # pissed off
            await message.channel.send(
                f"{ch(ref['angry_res'])} <@{msg_author}> {ch(ref['angry'])}."
            )

    # process the commands
    await client.process_commands(message)


@client.command(
        name="topic", aliases=["anything-interesting"],
        help="This function gives a topic from the science news for the week reported by LiveScience."
    )
async def topic(ctx):
    topic = function.give_topic()
    if not topic:
        await ctx.reply(
            f"sorry, the source is unfortunately down, please try again later... {ch(ref['sad'])}",
            mention_author=True
        )
    else:
        await ctx.reply(f"{dec} {ch(ref['surprised'])}", mention_author=True)


@client.command(
        name="define", aliases=["whatis", "def"],
        help="This defines a given word/phrase using the summary from wikipedia."
    )
async def wiki(ctx, word):
    mess, url = function.get_defin(word)

    if len(mess) > 1500:
        wc, delimiter, start = len(mess), 1500, 0

        while True:
            if wc > 1500 :
                if start == 0:
                    await ctx.reply(
                        f"Here you go <@{ctx.author.id}>! {ch(ref['happy'])}\n{mess[start:delimiter]}-",
                        mention_author=True
                    )
                else:
                    await ctx.channel.send(f"-{mess[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500

            elif wc < 1500:
                await ctx.channel.send(f"-{mess[start:delimiter+wc]}")
                await ctx.channel.send(url)
                break
    else:
        if not url:
            await ctx.reply(mess, mention_author=True)
        else:
            await ctx.reply(
                f"Here you go <@{ctx.author.id}>! {ch(ref['happy'])}\n{mess}\n{url}",
                mention_author=True
            )


@client.command(
        name="abs-bio", aliases=["fetch", "paper"],
        help="This returns the abstract of a given PubMed link."
    )
async def absBio(ctx, link):
    absBio, url = function.bio_abs(link)

    if len(absBio) > 1500:
        wc = len(absBio) ; delimiter = 1500 ; start = 0

        while True:
            if wc > 1500 :
                if start == 0:
                    await ctx.channel.send(
                        f"Here you go <@{ctx.author.id}>! {ch(ref['happy'])}\n{str(absBio)[start:delimiter]}-"
                    )
                else:
                    await ctx.channel.send(f"-{str(absBio)[start:delimiter]}-")
                start += 1500 ; delimiter += 1500 ; wc -= 1500

            elif wc < 1500:
                await ctx.channel.send(f"-{str(absBio)[start:delimiter+wc]}")
                await ctx.channel.send(url)
                break
    else:
        if not url:
            await ctx.channel.send(f"<@{ctx.author.id}> {absBio}")
        else:
            await ctx.channel.send(
                f"Here you go <@{ctx.author.id}>! {ch(ref['happy'])}\n{absBio}\n{url}"
            )


@client.command(
        name="src-code",
        help="Send the source code repository of the bot."
    )
async def src_code(ctx):
    await ctx.channel.send(
        f"Here you go {ch(ref['happy'])}!https://github.com/iaacornus/cornusbot",
        delete_after=60.0, mention_author=True
    )


client.run(TOKEN)
