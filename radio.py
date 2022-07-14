import discord
from discord.ext import commands
import youtube_dl
import ffmpeg

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel and then try again!")
        else:
            channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
                await ctx.send("Succesfully joined " + str(channel) + "!")
            else:
                await ctx.voice_client.move_to(channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from voice channel!")

    @commands.command()
    async def play(self, ctx, url):
       ydl_options = { 'format': 'bestaudio', 'noplaylist':   'True' }
       ffmpeg_options = { 'before_options': '-reconnect 1   -reconnect_streamed 1 -reconnect_delay_max 5',  'options': '-vn' }
       
       

def setup(bot):
    bot.add_cog(Radio(bot))

