import discord

from dotenv import load_dotenv
from discord.ext import commands
COMMAND_PREFIX = '##'
CHANNEL_ID = 690107427663904905 #Algemeen van de BRUHHHHH discord server



intents = discord.Intents.default()

load_dotenv()
TOKEN = "MTA4NjI4MzIxNTgxMzIxODM3NQ.Gln0Yn.xght6qFSImPqEe0idBJJiHgX7dAVz4-OfyvHFE" 

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print("Hallo, Brad is hier!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hallo, Brad is hier!")

@bot.command()
async def send(ctx, *, message: str):
    await ctx.send(message)


bot.run(TOKEN)
