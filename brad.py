import discord, os, requests, json, praw, pandas as pd, random



from dotenv import load_dotenv
from discord.ext import commands



COMMAND_PREFIX = '!'
CHANNEL_ID = 690107427663904905 #Algemeen van de BRUHHHHH discord server
load_dotenv() #Laad de token van de BOT in
TOKEN = os.environ["TOKEN"]
intents = discord.Intents.all()



#Voor de !aita command
ABSOLUTE_PATH = os.path.dirname(__file__)



bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)



@bot.event
async def on_ready():
    print("Hello, Brad has arrived!")
    channel = bot.get_channel(CHANNEL_ID)
    #await channel.send("Hello, Brad has arrived!\n Type '!helpme' to see what commands you can use.")



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



@bot.command()
async def chuck(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    response_text = response.text
    dict = json.loads(response_text)
    joke = dict['value']
    await ctx.send(f'{joke}')



@bot.command()
async def aita(ctx, arg1):
    arg1 = str(arg1)
    if arg1 not in ["hot", "new", "top"]:
        await ctx.send("Je hebt niet een geldige parameter gekozen voor !aita")
        return
    else:
        df = pd.DataFrame()
        user_agent = "Brad de meme verzamelaar"

        reddit = praw.Reddit(username="BradBotTheGoat", password="g!5$#TH$5!o@^aZmwrR@T3gH3&554^", client_id="eE_SvO-n5PmS4TjUg4qcDA", client_secret="AsvWTEPb5ZaACgprvHF_dBk3yT1Szg", user_agent=user_agent)
        subreddit_name = "AmItheAsshole"
        subreddit = reddit.subreddit(subreddit_name)
        if arg1 == "hot":
            submissions = subreddit.hot(limit=50)
        elif arg1 == "new":
            submissions = subreddit.new(limit=50)
        elif arg1 == "top":
            submissions = subreddit.top(limit=50)
        df = pd.DataFrame([{'title': s.title, 'selftext': s.selftext, 'upvote_ratio': s.upvote_ratio} for s in submissions])
        randompost = df.iloc[random.randint(0, 50)]
        randompost_title = randompost.loc['title']
        randompost_content = randompost.loc['selftext']

        await ctx.send(f'Deze post komt van de top 50 uit {arg1.upper()}')
        await ctx.send(f'Titel: {randompost_title}')
        if len(randompost_content) == 0:
            await ctx.send("Deze post had geen content")
    
        while len(randompost_content) > 0:
            if len(randompost_content) > 2000:
                await ctx.send(randompost_content[:2000])
                randompost_content = randompost_content[2000:]
            else:
                await ctx.send(randompost_content)
                randompost_content = ""
        await ctx.send(f"Deze post heeft een upvote ratio van {randompost.loc['upvote_ratio']} ")


@bot.command()
async def helpaita(ctx):
    await ctx.send("Doe !aita <hot> <new> <top> <")


bot.run(TOKEN)
