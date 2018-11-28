#! python3

# Weekly newsletter of top 5 posts of selected subreddits from past week

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import configparser
import schedule
import smtplib
import time
import praw

# Use configparser to read praw.ini file
config = configparser.ConfigParser()
config.read('praw.ini')

# Reddit account credentials
id = config['reddit']['client_id']
secret = config['reddit']['client_secret']
agent = config['reddit']['user_agent']
user = config['reddit']['username']
pwd = config['reddit']['password']

# Login using OAuth credentials
reddit = praw.Reddit(client_id = id,
                     client_secret = secret,
                     user_agent = agent,
                     username = user,
                     password = pwd)

# List of subscribed subreddits
subreddits = reddit.user.subreddits()
my_subs = []

for sub in subreddits:
    my_subs.append(sub.display_name)

# Collect: title - author - date - num. comments - url - upvotes - upvote_ratio
# Top 5 posts from last week for each subreddit
def weekly_top(num, sub_list):
    feed = ""

    for sub in sub_list:
        feed += '\n'.join(['\n', sub , '\n'])
        for post in reddit.subreddit(sub).top('week', limit = num):
            feed += '\n'.join([post.title, post.url])
            # TODO: continue with metadata to collect
            # UnicodeEncodeError

    return feed

weekly_top_1 = weekly_top(1, my_subs)
weekly_top_1 = str(weekly_top_1.encode('utf-8'))

# Email accounts setup
from_email = config['email_1']['email_address']
email_pwd = config['email_1']['email_password']
server = config['email_1']['smtp_server']
port = config['email_1']['smtp_port']

to_email = config['email_2']['email_address']

# Login in email
smtp = smtplib.SMTP(server, port)

smtp.ehlo()
smtp.starttls()
smtp.login(from_email, email_pwd)

message = '\r\n'.join([
  'From: %s' % (from_email),
  'To: %s' % (to_email),
  'Subject: Test',
  '',
  weekly_top_1])

smtp.sendmail(from_email, to_email, message)

smtp.quit()

# TODO: set up weekly email

def weekly_email():
    pass

# schedule.every(5).seconds.do(test)

# TODO: [OPTIONAL] Email markup and formatting
# TODO: [OPTIONAL] (GUI) customization of parameters
