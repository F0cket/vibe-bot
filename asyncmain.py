#usr/bin/env python

import discord
import time
import random
import ast
from discord.ext import commands

def parseUser(mentioned):
    ID = mentioned
    ID = ID.replace("<", "")
    ID = ID.replace("!", "")
    ID = ID.replace(">", "")
    ID = ID.replace("@", "")
    return ID

def writeVibes():
    with open("vibes.txt", 'w') as vibeFile:
        vibeFile.write(str(vibes))

def readVibes():
    with open("vibes.txt", 'r') as vibeFile:
        vibesString = vibeFile.read()
        return ast.literal_eval(vibesString)

def vibePercentageCalc(ID):
    vibeValueList = vibes[ID]
    return "{:.1%}".format(vibeValueList[0]/(vibeValueList[0] + vibeValueList[1]))

def setVibes(ID,PF):
    vibeValueList = vibes[ID]
    vibeValueList[PF] += 1
    writeVibes()

async def listVibeStats(vibes):
    message = ""
    for i in vibes:
        user = await bot.fetch_user(i)
        message += "{} -> {} good vibes\n".format(user.name, vibePercentageCalc(i))
    return message

bot = commands.Bot(command_prefix='!')

with open("DiscordToken.txt",'r') as tokenFile:
    token = str(tokenFile.readline()).replace("Token=","")

@bot.command(name='vibecheck', help='Check your own vibe or mention another user to check theirs.')
async def vibecheck(ctx, mentioned):
    ID = parseUser(mentioned)
    user = await bot.fetch_user(ID)
    print("[VIBECHECK] Author:", ctx.author, "Mentioned:",mentioned, "Name:", user.name)
    if ID not in vibes:
        vibes[ID] = [1,1]
    await ctx.channel.send("VIBECHECK! :gun: :gun: :gun:")
    time.sleep(1)
    if random.randint(1,2) == 1:
        setVibes(ID, 1)
        await ctx.channel.send("{} failed the vibecheck. You have {} good vibes.".format(user.name, vibePercentageCalc(ID)))
    else:
        setVibes(ID, 0)
        await ctx.channel.send("{} passed the vibecheck. You have {} good vibes.".format(user.name, vibePercentageCalc(ID)))
    print("[VIBECHECK COMPLETE] Author:", ctx.author, "Mentioned:",mentioned, "Name:", user.name)

@bot.command(name='vibestats', help="Check the vibe percentages")
async def vibestats(ctx):
    message = await listVibeStats(vibes)
    await ctx.channel.send("Current Vibes\n\n" + message)
    print("[VIBESTATS] Author:", ctx.author)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument) and ctx.invoked_with == "vibecheck":
        print("[WARNING] Author Mentioned No One. Using:", ctx.author.mention)
        await vibecheck(ctx, ctx.message.author.mention)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if random.randint(1,200) == 1:
        await message.add_reaction("⭐")
        await message.channel.send("Congratulations {}, your message is vibe-bot certified. Take this star as your reward. ⭐ It has no value.".format(message.author.name))
        time.sleep(2)
    await bot.process_commands(message)

vibes = readVibes()
bot.run(token)
