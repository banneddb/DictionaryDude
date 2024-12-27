import discord
from typing import Final
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

load_dotenv()
DICT_TOKEN = os.getenv('DICT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True  #Can read messages
bot = commands.Bot(command_prefix="?", intents=intents)

class GenCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, ):
        await ctx.send("Hello!")

    @commands.command()
    async def define(self, ctx, *, word: str):
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={DICT_TOKEN}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                definition = data[0].get('shortdef')
                await ctx.send(f"According to the Merriam-Webster Collegiate Dictionary,'{word}' can be best defined as {definition}")
            else:
                await ctx.send(f"No definition of {word} was found. Try again.")
        else:
            await ctx.send("There was an error processing your request. Try again.")

async def setup(bot):
   await bot.add_cog(GenCommands(bot))
   print("General commands succesfuly loaded")