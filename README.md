# Newsreddit

A Python script to turn your Reddit feed in an email with the top submissions for a given period.

### Introduction

This basic program lets you:

**1.** Create a list with your favourite subreddits 

**2.** Gets the top [n] submissions of the past [frequency] 

**3.** Sends you an email with the content 

### Requirements

You will need:

* **Reddit account**: Normal login + registration as a developer [here](https://www.reddit.com/prefs/apps/) 

* **OAuth credentials**: The process is well explained [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth). 

* **Email account**: Your email credentials, including SMTP server and port.

For convenience, I stored these in an .ini file locally and used <code>configparser</code> to access them for the script.  
I included an .ini file template in this repo, and as you can see it is really easy to use.  
Feel free to adapt this script to whatever method you use to store your credendials. Stay safe, folks!  

### Dependencies

* [PRAW](https://praw.readthedocs.io/en/latest/) (Python Reddit API Wrapper) 

* [Arrow](http://arrow.readthedocs.io/) (Human-friendly library for dates, times, and timestamps) 

* [Unidecode](https://pypi.org/project/Unidecode/) (Transform Unicode characters in their closest ASCII representation)

To install, <code>pip install [module_name]</code> should do the trick for all of them. 

### Schedule

To make the most out of this script, I would recommend using it to turn it into a **scheduled task**. 

In Windows, you can simply create a scheduled job in <code>Task Scheduler</code> to run the script every day/week/month etc. 

In my case, I am using this to have a weekly email with the top 5 posts of the week from my favourite subreddits.

### Improvements

This program can be improved with additional features:

**1. User login**

For safer one-off use, credentials could be entered manually.

**2. Email format**

Add some colour to the minimalistic plaintext using an HTML email.

**3. Customization**

Add possibility to use optional arguments to change basic parameters such as:

* **Frequency** of top posts fetched (see PRAW documentation for available option)

* **Number** of posts to retrieve (being mindful of Reddit API limitations)

* **Subreddits** list (adding / removing custom subs)

**4. GUI**

All the above, but with a fancy user interface. 
