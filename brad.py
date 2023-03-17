import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

COMMAND_PREFIX = '##'
CHANNEL_ID = 690107427663904905 #Algemeen van de BRUHHHHH discord server
load_dotenv() #Laad de token van de BOT in
TOKEN = os.environ["TOKEN"]
intents = discord.Intents.default()

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print("Hallo, Brad is hier!")
    channel = bot.get_channel(CHANNEL_ID)
    #await channel.send("Hallo, Brad is hier!")

@bot.command()
async def send(ctx, *, message: str):
    await ctx.send(message)


bot.run(TOKEN)
