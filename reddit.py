import praw
import pandas as pd
import random
def praw_scraper():
    df = pd.DataFrame()
    user_agent = "Brad de meme verzamelaar"

    reddit = praw.Reddit(username="BradBotTheGoat", password="g!5$#TH$5!o@^aZmwrR@T3gH3&554^", client_id="eE_SvO-n5PmS4TjUg4qcDA", client_secret="AsvWTEPb5ZaACgprvHF_dBk3yT1Szg", user_agent=user_agent)
    subreddit_name = "AmItheAsshole"
    subreddit = reddit.subreddit(subreddit_name)
    
    titles=[]
    selftexts=[]
    submissions= subreddit.hot(limit=50)
    for submission in submissions:
        titles.append(submission.title)
        selftexts.append(submission.selftext)
        
    df['Title'] = titles
    df['Content'] = selftexts
    
    print(df.shape) 
    randompost = df.iloc[random.randint(0, 30)]
    randompost_title = randompost.loc['Title']
    randompost_content = randompost.loc['Content']


praw_scraper()

   
    
    
    
    
    
    
    