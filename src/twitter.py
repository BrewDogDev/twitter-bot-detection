import time

import tweepy

import keys
import dataHandler

#authenticate with twitter
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


dataFile = "src/data/twitter_human_bots_dataset.csv"
data = dataHandler.getDataFrame(dataFile)

for index, user in data.iterrows():
    try:
        print(index)
        userInfo = api.get_user(user_id = user['id'])
        print(userInfo.screen_name)
        userInfo.screen_name
    except Exception as e: #account probably banned
        print(e)
        pass
    