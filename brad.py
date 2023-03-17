import discord
from discord.ext import commands

def main():

    bot = commands.Bot(command_prefix='!', token='MTA4NjI4MzIxNTgxMzIxODM3NQ.Gln0Yn.xght6qFSImPqEe0idBJJiHgX7dAVz4-OfyvHFE')

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello!')

    bot.run('MTA4NjI4MzIxNTgxMzIxODM3NQ.Gln0Yn.xght6qFSImPqEe0idBJJiHgX7dAVz4-OfyvHFE')

if __name__ == "__main__":
    main()