from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# Loading the token into the program
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)