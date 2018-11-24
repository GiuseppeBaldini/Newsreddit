#! python3

# Weekly newsletter of top 5 posts of selected subreddits from past week

import configparser
import praw

# Use configparser to read praw.ini file
config = configparser.ConfigParser()
config.read('praw.ini')

# Credentials
id = config['newsreddit']['client_id']
secret = config['newsreddit']['client_secret']
agent = config['newsreddit']['user_agent']
user = config['newsreddit']['username']
pwd = config['newsreddit']['password']

# Login using OAuth credentials
reddit = praw.Reddit(client_id = id,
                     client_secret = secret,
                     user_agent = agent,
                     username = user ,
                     password = pwd)

# List of subscribed subreddits
subreddits = reddit.user.subreddits()
subs = []

for sub in subreddits:
    subs.append(sub.display_name)

# Top 5 posts from last week for each subreddit
for sub in subs:
    for post in reddit.subreddit(sub).top('week', limit = 5):
        print(post.title)

# TODO: collect links + titles + metrics (upvotes + comments)

# TODO: create email template sorting (alphabetically) by subreddit

# TODO: set up weekly email

# TODO: [OPTIONAL] Email markup and formatting
# TODO: [OPTIONAL] (GUI) customization of parameters
