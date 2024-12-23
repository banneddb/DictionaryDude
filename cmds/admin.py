import discord
from typing import Final
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  #Can read messages
bot = commands.Bot(command_prefix="?", intents=intents)
statusChannel = 1319479548013711461

commandsList= {"?shutdown": "Shuts down the bot",
                "?define": "Defines a word",
                "?hello" : "Simple hello back"
                }
@bot.command()
async def shutdown(ctx):
    if ctx.channel.id == statusChannel:
        if ctx.author.id == 275064408940740630:
            await ctx.send("Bot is shutting down and offline.")
            await bot.close()
            print("Successfully logged out")
        else:
            await ctx.send("You do not have permission to shutdown the bot.")
    else:
        await ctx.send("You can only shut down the bot in #bot-status")

@bot.command()
async def bothelp(ctx):
    response = "\n".join([f"{command}: {description}" for command, description in commandsList.items()])
    await ctx.send("Here is a list of commands:")
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Send ?bothelp for more information.")
