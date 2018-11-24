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

print('I am ' + str(reddit.user.me()))

# TODO: list of subreddits of interest

# TODO: find 5 posts from last week for each subreddit

# TODO: retrieve links + titles + metrics (upvotes + comments)

# TODO: create email template sorting (alphabetically) by subreddit

# TODO: set up weekly email

# TODO: [OPTIONAL] Email markup and formatting
# TODO: [OPTIONAL] (GUI) customization of parameters
