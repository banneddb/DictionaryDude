import discord
from typing import Final
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  #Can read messages
bot = commands.Bot(command_prefix="?", intents=intents)

class GenCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")


async def setup(bot):
    await bot.add_cog(GenCommands(bot))
    print("General commands succesfuly loaded")
