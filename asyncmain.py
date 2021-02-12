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


@bot.command(name='vibecheck', help='Ensure your vibe is in check.')
async def vibecheck(message):
    await message.send("VIBECHECK! :gun: :gun: :gun:")
    time.sleep(1)
    if random.randint(1,3) == 1:
        await message.send("{} failed the vibecheck.".format(message.author.name))
    else:
        await message.send("{} passed the vibecheck.".format(message.author.name))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Sorry {}. I need {} more minutes to get another meme. Reddit doesn't like me scraping images so quickly.".format(ctx.author.name, round(round(error.retry_after)/60)))



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
