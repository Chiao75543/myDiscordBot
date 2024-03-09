import discord
from discord.ext import commands,tasks
from datetime import datetime
import json

# emoji url:http://www.get-emoji.com

class poll_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.emoji = ['1\u1F40C','2\u1F4A','3\u26F5','4\u1F608','5\u1F35A']
    
    @commands.command()
    # @commands.has_permissions(administrator = True)
    async def poll(self,ctx,vote:int ,title ,*options):
        await ctx.send("123")




async def setup(bot):
    await bot.add_cog(poll_cog(bot))