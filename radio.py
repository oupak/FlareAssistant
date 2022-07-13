import discord
from discord.ext import commands
import youtube_dl

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel and then try again!")
        else:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
            else:
                await ctx.voice_client.move_to(channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def add(self, ctx):
       pass

def setup(bot):
    bot.add_cog(Radio(bot))

