import discord
from typing import Final
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISC_TOKEN')
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="?", intents=intents)

print(TOKEN)
@bot.event
async def on_ready():
    print('Successfully logged in and booted')

bot.run(TOKEN)
