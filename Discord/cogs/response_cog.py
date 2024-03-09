import discord
from discord.ext import commands

# https://www.htmlcsscolor.com

class response_cog (commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.help_message = """
```
General Command:
/rule : Server rules.
/help : Show available commands.
/tips : Read how to get a girlfriend.
/play [url]:Search music in youtube and play it. 
/queue : Show the music queue.
/skip : Skip current music.
/clear : Clear the music queue.
/disconnect : Disconnect the voice channel.
/pause : Pause the msuic.
/resume : Resume the music.
/chat : Chat with chatgpt.
/exit : Bot will be offline in a few minute.

現在這機器人有時候有點問題,不知道是怎樣,但我懶得改,不要用playlist應該都還好。
```
"""

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[大蝸牛] is online.")

    @commands.Cog.listener()
    async def on_message(self,message):
        friend = ["有局嗎","今天有嗎","今天有局嗎","有橘嗎"]
        for words in friend:
            if message.content.find(words) >= 0 and message.author != self.bot.user :
                 await message.channel.send("有 幾點")
                 break

    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send('Bot error:'+error)

    @commands.command()
    async def help(self,ctx):
        await ctx.send(self.help_message)

    @commands.command()
    async def tips(self,ctx):
        embed_tip = discord.Embed(title="豹哥掌握女人的招式",
        description="""

1.看星星
2.調情
3.偷記人家生理期再送東西
4.拍她好看照片
5.過馬路把她拉過來 靠近自己
6.天冷袋個暖暖包
7.隨身攜帶ok蹦
8.要記喜好
9.偷記他喜歡的東西跟不喜歡的東西在手機筆記裡 然後再假裝不經意讓他看見妳有記錄這些
10.傳了八成也沒事再衝 不然我手機還會放一個我其他朋友的紀錄 讓我有後路說 我都會記好朋友的喜好生日禮物好送
11.穿搭真的挺重要的
12.選一款自己的香水
13.幫女生卸妝
14.做超可愛便當

"""
        ,color=0xFF3375)
        embed_tip.set_author(name='bakemonono',icon_url="https://cdn.discordapp.com/avatars/732601055166202000/7e2db3f2ed0441245c52479160eecbc4.webp?size=128")
        await ctx.send(embed = embed_tip)


    @commands.command()
    async def rule(self,ctx):
        rule = discord.Embed(title="詹姆士心意已決永不背叛",
        description="這是最好兄弟最真心的詹姆士團隊的誓言"
        ,color=0xFF3375)
        
        rule.add_field(name="絕不背叛兄弟",value="禁止戴兄弟綠帽、禁止內鬼。",inline=False)
        rule.add_field(name="絕不碰憂鬱症",value="這裡有慘痛的例子。")
        rule.add_field(name="絕不暈船",value="這裡有很多慘痛的例子。")

        await ctx.send(embed = rule)


    @commands.command()
    async def exit(self,ctx):
        await ctx.send('Bot will be offline in a few minute.')
        await self.bot.change_presence(status=discord.Status.offline)
        await exit()

    @commands.command()
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel")
        else:
            channel = ctx.author.voice.channel
            await channel.connect()


async def setup(bot):
    await bot.add_cog(response_cog(bot))
