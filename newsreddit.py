#! python3

# Weekly newsletter of top posts of selected subreddits from past week

from unidecode import unidecode
import configparser
import smtplib
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

def weekly_top(num, sub_list):
    feed = ""

    for sub in sub_list:
        feed += '\n'.join([('--' * len(sub)) , sub , ('--' * len(sub)), '\n'])
        for post in reddit.subreddit(sub).top('week', limit = num):
            feed += '\n'.join([post.title, post.url, '\n'])

    return feed

weekly_top_1 = weekly_top(1, my_subs)

weekly_top_1 = '''
'''.join(weekly_top_1.splitlines())

weekly_top_1 = unidecode(weekly_top_1)

# Email function
def email(sender, password, smtp_server, smtp_port, receiver, content):

    smtp = smtplib.SMTP(smtp_server, smtp_port)

    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, password)

    message = '\r\n'.join([
      'From: %s' % (sender),
      'To: %s' % (receiver),
      'Subject: Newsreddit',
      '',
      content])

    smtp.sendmail(sender, receiver, message)

    smtp.quit()

# Email accounts setup
from_email = config['email_1']['email_address']
email_pwd = config['email_1']['email_password']
server = config['email_1']['smtp_server']
port = config['email_1']['smtp_port']

to_email = config['email_2']['email_address']

# Send email
def send_email():
    email(from_email, email_pwd, server, port, to_email, weekly_top_1)

# Set up weekly email (Task Scheduler)
