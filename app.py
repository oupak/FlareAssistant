from secrets import token_hex
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import radio
import image_from_text
import chat

load_dotenv()

token = os.environ.get('token')

activity = discord.Activity(type=discord.ActivityType.watching, name='//info')

bot = commands.Bot(command_prefix='//', activity=activity)
radio.setup(bot)
image_from_text.setup(bot)
chat.setup(bot)

@bot.event
async def on_ready():
    print('Bot successfully connected')

@bot.command()
async def hello(ctx):
    await ctx.send("hello!")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Info", description="Reply or mention me to have a conversation!", color=0xff0000)
    embed.add_field(name="Radio commands", value="//join - Join the voice channel\n//play <youtube link> - Play a song\n//disconnect - Disconnect from the voice channel", inline=False)
    await ctx.send(embed=embed)

bot.run(token)
