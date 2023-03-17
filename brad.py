import discord
from discord.ext import commands

def main():

    bot = commands.Bot(command_prefix='!', token='MTA4NjI4MzIxNTgxMzIxODM3NQ.Gn7ywL.eb2-Fxey3J3D0sFFgG1uLs2j5MY7rEZcx9LP0s')

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello!')

    bot.run('MTA4NjI4MzIxNTgxMzIxODM3NQ.Gn7ywL.eb2-Fxey3J3D0sFFgG1uLs2j5MY7rEZcx9LP0s')

if __name__ == "__main__":
    main()