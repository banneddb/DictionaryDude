import discord
from typing import Final
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
import time
import datetime

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
        await ctx.send("Fetching information....")
        time.sleep(2)
        if response.status_code == 200:
            data = response.json()
            if data:
                definitionList = data[0].get('shortdef')
                #exampleList = data[0].get('examples:')
                definition = str(definitionList[0])
                embed = discord.Embed(
                    title = word.capitalize(),
                    description= definition.capitalize(),
                    color=discord.Color.blue()
                )
                embed.add_field(name="Part of Speech", value= data[0].get('fl') , inline=False)
                embed.add_field(name="Synonyms", value = "WIP", inline=True)
                embed.add_field(name="Example", value="WIP", inline=False)
                embed.set_thumbnail(url="https://merriam-webster.com/assets/mw/static/app-css-images/logos/mw-logo.png")
                embed.timestamp = datetime.datetime.now()
                embed.set_footer(text="Retrieved from the Merriam-Webster's Collegiate Dictionary")
                embed.set_author(name =f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            elif len(data) == 0:
                await ctx.send(f":warning: No definition of {word} was found! Try again.")
        else:
            await ctx.send("There was an error processing your request. Try again.")

async def setup(bot):
   await bot.add_cog(GenCommands(bot))
   print("General commands succesfuly loaded")