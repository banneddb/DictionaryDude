import discord
from typing import Final
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISC_TOKEN')
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



async def main():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cmds.{filename[:-3]}')
            except Exception as e:
                print(f'Error loading cmds {filename}:\n{e}')
    await bot.start(TOKEN)

asyncio.run(main())
