#! python3

# Weekly newsletter of top reddit posts from previous week

from unidecode import unidecode
import configparser
import smtplib
import arrow
import praw

# Use configparser to read praw.ini file
config = configparser.ConfigParser()
config.read('setup.ini')

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

def top_posts(frequency, num, sub_list):
    '''
    Get [frequency] top [num] posts of each subreddit in [sub_list] in format:

    --------------
    subreddit_name
    --------------
    [Post_title]
    [Post_ url]

    '''
    feed = ""
    for sub in sub_list:
        feed += '\n'.join([('--' * len(sub)) , sub , ('--' * len(sub)), '\n'])
        for post in reddit.subreddit(sub).top(frequency, limit = num):
            feed += '\n'.join([post.title, post.url, '\n'])

    return feed

# Get weekly top 5 posts from my subreddits
weekly_top_5 = top_posts('week', 5, my_subs)

# To avoid encoding issues, use normal space instead of newline \n
weekly_top_5 = '''
'''.join(weekly_top_5.splitlines())

# Unidecode transforms Unicode characters to their closest ASCII representation
weekly_top_5 = unidecode(weekly_top_5)

# Specify date to use in our email subject
date = arrow.now('Europe/Rome').format('DD/MM/YYYY')

# Email function
def email(sender, password, smtp_server, smtp_port, receiver, content):

    smtp = smtplib.SMTP(smtp_server, smtp_port)

    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, password)

    message = '\r\n'.join([
      'From: %s' % (sender),
      'To: %s' % (receiver),
      'Subject: Newsreddit - %s' % (date),
      '',
      content])

    smtp.sendmail(sender, receiver, message)

    smtp.quit()

# Email accounts credentials
from_email = config['email_1']['email_address']
email_pwd = config['email_1']['email_password']
server = config['email_1']['smtp_server']
port = config['email_1']['smtp_port']

to_email = config['email_2']['email_address']

# Send email
email(from_email, email_pwd, server, port, to_email, weekly_top_5)
