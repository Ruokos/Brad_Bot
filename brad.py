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
async def calc(ctx, *arr):
    result = int(arr[1])
    if arr[0] == "+":
        for i in arr[2:]:
            result += int(i)
    elif arr[0] == "/":
        for i in arr[2:]:
            result /= int(i)
    elif arr[0] == "*":
        for i in arr[2:]:
            result *= int(i)
    elif arr[0] == "-":
        for i in arr[2:]:
            result -= int(i)
    await ctx.send(f'Result: {result}')



@bot.command()
async def helpme(ctx):
    await ctx.send("I abide by these commands:\n!brad\n!helpme\n!calc\n!sex\n!hello\n\nIf you want info on the syntax of these commands, type '!help<command>'.")

@bot.command()
async def helpcalc(ctx):
    await ctx.send("!calc <operator> <numbers spaced by blank spaces>")

@bot.command()
async def helpbrad(ctx):
    await ctx.send("!brad")

@bot.command()
async def helphelpme(ctx):
    await ctx.send("!helpme")

@bot.command()
async def helpsex(ctx):
    await ctx.send("!sex")

@bot.command()
async def helphello(ctx):
    await ctx.send("!sex")

@bot.command()
async def sex(ctx):
    await ctx.send(f"*Has sex with {ctx.message.author.mention}*",)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.message.author.mention}, how are you?",)

bot.run(TOKEN)
