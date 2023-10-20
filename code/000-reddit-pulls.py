#!/usr/bin/env python
# coding: utf-8

#this is just the scraper so I can get multiple lots of posts



import pandas as pd
import time
import praw


# I chose not to care about keeping these credentials secret
# This is a throwaway account & I will be changing the password.
reddit = praw.Reddit(
    client_id='MpNNGXPo1W7O7AeAMpjRuA',
    client_secret='v85vo5HC61pn_rZQZS77GDtOlkntTQ',
    user_agent='DSI911 class project script by /u/Creative-Abalone-483',
    username='Creative-Abalone-483',
    password='klar-rox_FLEE1grog'
)

#print(reddit.user.me())




# Choose your subreddit
#currently using explainlikeimfive & nostupidquestions

sub1reddit = reddit.subreddit('explainlikeimfive')
# Adjust the limit as needed -- Note that this will grab the 25 most recent posts
sub1posts = sub1reddit.new(limit=1000)


#for the next one
sub2reddit = reddit.subreddit('nostupidquestions')
sub2posts = sub2reddit.new(limit=1000)




data = []
for post in sub1posts:
    data.append([post.created_utc, post.title, post.selftext, post.subreddit])

# Turn sub1's data into a dataframe
df_sub1 = pd.DataFrame(data, columns = ['created_utc', 'title', 'self_text', 'subreddit'])


#df_sub1[ df_sub1['self_text'] != ''].shape


#drop full row if self_text is empty string
#attrib - chatgpt bc I was driving myself crazy
column_to_check = "self_text"
df_sub1 = df_sub1[ df_sub1[column_to_check] != '' ]



now_tag = round(time.time())
filename = "../data/sub1-"+str(now_tag)+".csv"

# and save current (no-empty-posts) state to a timestamped file
df_sub1.to_csv(filename)



data = []
for post in sub2posts:
    data.append([post.created_utc, post.title, post.selftext, post.subreddit])

# Turn sub2 results into a dataframe
df_sub2 = pd.DataFrame(data, columns = ['created_utc', 'title', 'self_text', 'subreddit'])


#drop full row if self_text is empty string
column_to_check = "self_text"
df_sub2 = df_sub2[ df_sub2[column_to_check] != '' ]

# and save current (no-empty-posts) state to a timestamped file
now_tag = round(time.time()) #note that the rounding will also limit my rate
filename2 = "../data/sub2-"+str(now_tag)+".csv"
df_sub2.to_csv(filename2)

