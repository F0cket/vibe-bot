import discord
import time
import random
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

with open("DiscordToken.txt",'r') as tokenFile:
    token = str(tokenFile.readline()).replace("Token=","")

@bot.command(name='vibecheck', help='Check your own vibe or mention another user to check theirs.')
async def vibecheck(ctx, mentioned):
    ID = mentioned
    ID = ID.replace("<", "")
    ID = ID.replace("!", "")
    ID = ID.replace(">", "")
    ID = ID.replace("@", "")
    user = await bot.fetch_user(ID)
    print("[VIBECHECK] Author:", ctx.author, "Mentioned:",mentioned, "Name:", user.name)
    await ctx.channel.send("VIBECHECK! :gun: :gun: :gun:")
    time.sleep(1)
    if random.randint(1,2) == 1:
        await ctx.channel.send("{} failed the vibecheck.".format(user.name))
    else:
        await ctx.channel.send("{} passed the vibecheck.".format(user.name))
    print("[VIBECHECK COMPLETE] Author:", ctx.author, "Mentioned:",mentioned, "Name:", user.name)

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

    
bot.run(token)
