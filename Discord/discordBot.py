import discord
import os
from dotenv import load_dotenv


client = discord.Client(intents=discord.Intents.default())
load_dotenv()

# Bot launch
@client.event
async def on_ready():
    print("now login:",client.user)
    await client.change_presence(status=discord.Status.online , activity = discord.Game('屁眼'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return



client.run(os.getenv("DISCORD_TOKEN"))