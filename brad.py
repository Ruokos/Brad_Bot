import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

COMMAND_PREFIX = '!'
CHANNEL_ID = 690107427663904905 #Algemeen van de BRUHHHHH discord server
load_dotenv() #Laad de token van de BOT in
TOKEN = os.environ["TOKEN"]
intents = discord.Intents.all()


bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print("Hello, Brad has arrived!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello, Brad has arrived!\n Type '!helpme' to see what commands you can use.")

@bot.command()
async def brad(ctx):
    await ctx.send("I am Brad")

@bot.command()
async def sum(ctx, *arr):
    result = 0
    if arr[0] == "+":
        for i in arr[1:]:
            result += int(i)
    elif arr[0] == "/":
        for i in arr[1:]:
            result /= int(i)
    elif arr[0] == "*":
        for i in arr[1:]:
            result *= int(i)
    elif arr[0] == "-":
        for i in arr[1:]:
            result -= int(i)
    await ctx.send(f'Result: {result}')



@bot.command()
async def helpme(ctx):
    await ctx.send("I abide by these commands:\n!brad\n!helpme\n!sum")



bot.run(TOKEN)
