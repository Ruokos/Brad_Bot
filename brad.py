import discord
from dotenv import load_dotenv

intents = discord.Intents.default()

load_dotenv()
TOKEN = "MTA4NjI4MzIxNTgxMzIxODM3NQ.Gln0Yn.xght6qFSImPqEe0idBJJiHgX7dAVz4-OfyvHFE" 

client = discord.Client(intents=intents)

@bot.command()
    async def hello(ctx):
        await ctx.send('Hello! I am Brad!')

@client.event
async def on_ready():
    print(f'{client.user} is verbonden met Discord!')

client.run(TOKEN)
