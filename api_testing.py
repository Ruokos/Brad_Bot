import discord, os, requests, json, praw, pandas as pd, random, openai



from dotenv import load_dotenv
from discord.ext import commands



COMMAND_PREFIX = '!'
CHANNEL_ID = 690107427663904905 #Algemeen van de BRUHHHHH discord server
load_dotenv() #Laad de token van de BOT in
TOKEN = os.environ["TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
intents = discord.Intents.all()
openai.api_key = OPENAI_API_KEY


#Voor de !aita command
ABSOLUTE_PATH = os.path.dirname(__file__)



bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.command()
async def summarise(ctx):
    data = pd.DataFrame(columns=['content', 'author'])
    history_prompt = "The history of this chat went as following:"
    async for msg in ctx.channel.history(limit=20):
        msg_author_name = str(msg.author.name)
        msg_content = str(msg.content)
        if msg.author.bot == True:
            pass
        else:
            history_prompt = history_prompt + f"{msg_author_name} said: {msg.content}"
            print(history_prompt)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        max_tokens = 2000,
        messages = [
        {"role": "system", "content": history_prompt},
        {"role": "user", "content": 'Can you summarise the history of the chat for me?'}
            ]
        )
    chatgpt_response = response['choices'][0]['message']['content']
    await ctx.send(f"{chatgpt_response}")
            
    
bot.run(TOKEN)