import discord
import openai
from discord.ext import commands
from pychatgpt import ChatGPT
from dotenv import load_dotenv,dotenv_values
import os

# https://beta.openai.com/docs/models/overview
# https://github.com/Lanznx/HealthLineBot?fbclid=IwAR2_Ha7y_I5A9r5Z64GXxk8OI4FeXDSi7MEOjDDfPfduWSVbju2RFoyFIgI&mibextid=Zxz2cZ

load_dotenv()
ENV_PATH = 'D:\MyPythonProject\Discord\.env'
CHAT_GPT_TOKEN = dotenv_values(ENV_PATH)["CHATGPT_API_KEY"]

class chat_cog (commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def chat(self,ctx,*args):
        chat_message = " ".join(args)

        openai.api_key = CHAT_GPT_TOKEN
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = chat_message,
            max_tokens = 1000,
            temperature = 0.8
        )
        print(response['choices'][0]['text'])

        await ctx.send(response['choices'][0]['text'])

async def setup(bot):
    await bot.add_cog(chat_cog(bot))
