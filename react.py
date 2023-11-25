import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
SERVER_ID = os.getenv('SERVER')
CHANNEL_ID = os.getenv('CHANNEL')
TARGET_WORD = os.getenv('TARGET')
REACTION_EMOJI = os.getenv('EMOJI')

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    try:
        if (
            message.guild.id == SERVER_ID
            and message.channel.id == CHANNEL_ID
            and TARGET_WORD in message.content.lower()
        ):
            print(f"Received target message: {message.content}")
            emoji = REACTION_EMOJI
            await message.add_reaction(emoji)
            print("Reacted to message")
    except Exception as e:
        print(e)

client.run(TOKEN)
