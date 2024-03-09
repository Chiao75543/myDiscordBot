import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

MY_BOT_ACTIVITY = 'Type /help to check commands.'

load_dotenv()

intent = discord.Intents.all()
intent.members = True
bot = commands.Bot(command_prefix='/',intents=intent)

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(MY_BOT_ACTIVITY))


async def load():
        for filename in os.listdir('Discord\cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(os.getenv("DISCORD_TOKEN"))        

asyncio.run(main())


