import discord
from discord.ext import commands
import asyncpraw
import time
import random
from datetime import datetime


r = asyncpraw.Reddit("vibe-bot",user_agent = "meme_grabber v1.0")
bot = commands.Bot(command_prefix='!')
usedMemesID = []

with open("DiscordToken.txt",'r') as tokenFile:
    token = str(tokenFile.readline()).replace("Token=","")

async def starMeme():
    subreddit = await r.subreddit('starwarsmemes')
    async for post in subreddit.hot(limit = 15):
        url = str(post.url)
        if post.id in usedMemesID:
            continue
        else:
            usedMemesID.append(post.id)
            return url

async def dankMeme():
    if random.randint(1,2) == 1:
        subreddit = await r.subreddit('memes')
    else:
        subreddit = await r.subreddit('dankmemes')
    async for post in subreddit.hot(limit = 15):
        url = str(post.url)
        if post.id in usedMemesID:
            continue
        else:
            usedMemesID.append(post.id)
            return url


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith("!") and random.randint(1,200) == 1:
        await message.add_reaction("⭐")
        await message.channel.send("Congratulations {}, your message is vibe-bot certified. Take this star as your reward. ⭐ It has no value.".format(message.author.name))
    await bot.process_commands(message)

@bot.command(name='vibecheck', help='Check your own vibe or mention another user to check theirs.')
async def vibecheck(ctx, mentioned):
    user = await bot.fetch_user(mentioned[3:-1])
    if user.name.startswith("!"):
        user.replace("!","")
    if mentioned.startswith("<@!"):
        await ctx.send("VIBECHECK! :gun: :gun: :gun:")
        time.sleep(1)
        if random.randint(1,3) == 1:
            await ctx.send("{} failed the vibecheck.".format(user.name))
        else:
            await ctx.send("{} passed the vibecheck.".format(user.name))
    else:
        await ctx.send("Make sure to mention a user when running the command.")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown) and ctx.invoked_with == "meme" or ctx.invoked_with == "starmeme":
        await ctx.send("Sorry {}. I need {} more seconds to get another meme. Reddit doesn't like me scraping images so quickly.".format(ctx.author.name, round(error.retry_after)))
    if isinstance(error, commands.MissingRequiredArgument) and ctx.invoked_with == "vibecheck":
        await vibecheck(ctx, ctx.message.author.mention))
    raise error


@bot.command(name='starmeme',help = "Get a meme from the starwars subreddit.")
@commands.cooldown(5,60)
async def getstarMeme(ctx):
    url = await starMeme()
    await ctx.send(url)


@bot.command(name='meme',help = "Get a meme from reddit")
@commands.cooldown(5,60)
async def getdankMeme(ctx):
    url = await dankMeme()
    await ctx.send(url)


@bot.command(name='sandstorm', help = "dun dun dun dun dun")
async def playSandstorm(ctx):
    await ctx.send("https://www.youtube.com/watch?v=y6120QOlsfU")

bot.run(token)
