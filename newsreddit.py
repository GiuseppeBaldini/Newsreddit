#! python3

# Weekly newsletter of top 5 posts of selected subreddits from past week

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
    for sub in sub_list:
        print('''--- \n%s \n---''' % (sub))
        for post in reddit.subreddit(sub).top('week', limit = num):
            print(post.title)
            print(post.url)
            # TODO: continue with data to collect

# weekly_top_1 = weekly_top(1, my_subs)

# Email accounts setup
from_email = config['email']['email_address']
email_pwd = config['email']['email_password']
server = config['email']['smtp_server']
port = config['email']['smtp_port']
to_email = config['email']['receiver_email']


# Login in email
smtp = smtplib.SMTP(server, port)

smtp.ehlo()
smtp.starttls()
smtp.login(email, email_pwd)

message = '\r\n'.join([
  'From: %s' % (from_email),
  'To: %s' % (to_email),
  'Subject: Test',
  "",
  "A message."
  ])

# smtp.sendmail(email, 'giuseppebaldini@live.com', message)

smtp.quit()

# TODO: set up weekly email

def test():
    print('Testing.. ')

schedule.every(5).seconds.do(test)

while True:
    schedule.run_pending()

# TODO: [OPTIONAL] Email markup and formatting
# TODO: [OPTIONAL] (GUI) customization of parameters
