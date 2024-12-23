import discord
from typing import Final
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  #Can read messages
bot = commands.Bot(command_prefix="?", intents=intents)
statusChannel = 1319479548013711461

@bot.event
async def on_ready():
    channel = bot.get_channel(statusChannel)
    if channel is not None:
        await channel.send("Bot is online.")
    print('Successfully logged in')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! 👋")

