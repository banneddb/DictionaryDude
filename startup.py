from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from blackjackcode import black_jack

# Loading the token into the program
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot set-up below
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

# Dictionary to track progress for each user or channel
game_states = {}
# Reading messages
async def send_message(message: Message, user_message:str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled)")
        return
    if user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response: str = black_jack(user_message)
        await message.author.send(response) if user_message[0] == '?' else await message.channel.send(response)
    except Exception as e:
        print(e)

# Start-up for the Bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = (message.content)
    channel_id: str = str(message.channel.id)

    print(f'[{channel_id}] {username}: "{user_message}"')
    if channel_id not in game_states:
        game_states[channel_id] = {'in_progress': False, 'player_choice': None, 'player_total':0, 'player_cards': []}
    if user_message.startswith("play blackjack"):
        if game_states[channel_id]['in_progress']:
            await message.channel.send("A game is already in progress.")
        else:
            game_states[channel_id]['in_progress'] = True
            game_states[channel_id]['player_choice'] = None
            game_states[channel_id]['player_total'] = 0
            game_states[channel_id]['player_cards'] = []
            game_response = black_jack(start_new=True, state=game_states[channel_id])
            await message.channel.send("\n".join(game_response))
    elif user_message in ["1","11","hit","stay"]:
        if not game_states[channel_id]['in_progress']:
            await message.channel.send("No game in progress. Send 'play blackjack' to start the game!")
        else:
            game_states[channel_id]['player_choice'] = user_message
            game_response = black_jack(player_choice=user_message, state=game_states[channel_id])
            await message.channel.send("\n".join(game_response))
            if any("Game over" in msg for msg in game_response) or "You win" in game_response:
                game_states[channel_id]['in_progress'] = False

    else:
        await message.channel.send("Send 'play blackjack' to start the game!")
client.run(TOKEN)