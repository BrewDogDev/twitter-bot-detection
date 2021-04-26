import time

import pandas
import tweepy


import keys
import dataHandler


#authenticate with twitter
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


dataFile = "data/twitter_human_bots_dataset.csv"
old_data = dataHandler.getDataFrame(dataFile)

myColumns = ["name", "screen_name", "Location", "protected", "creation_date", "description", "followers_count", "following_count", "favorites_count", "tweets_count", "verified", "tweet1_text", "tweet1_date", "tweet2_text", "tweet2_date", "tweet3_text", "tweet3_date", "tweet4_text", "tweet4_date", "tweet5_text", "tweet5_date", "is_bot" ]
new_data = pandas.DataFrame(columns=myColumns)
print(new_data)

for index, user in old_data.iterrows():
    try:
        if index%900 == 0 and index !=0:
            dataHandler.makeCSV(new_data, index)
            time.sleep(60*10)

        user_id = user['id']
        is_bot = True if user['account_type'] == 'bot' else False

        userInfo = api.get_user(user_id)
        userTimeline = api.user_timeline(user_id, count = 5)
        
        tweets_text = []
        tweets_date = []
        for i in range(0,5):
            try:
                tweets_text.append(userTimeline[i].text)
                tweets_date.append(userTimeline[i].created_at)
            except Exception as e:
                print("not many tweets", index)
                tweets_text.append("")
                tweets_date.append("")
            


        new_row = [userInfo.name, userInfo.screen_name, userInfo.location, userInfo.protected, userInfo.created_at, userInfo.description, userInfo.followers_count, userInfo.friends_count, userInfo.favourites_count, userInfo.statuses_count, userInfo.verified, tweets_text[0], tweets_date[0], tweets_text[1], tweets_date[1], tweets_text[2], tweets_date[2], tweets_text[3], tweets_date[3], tweets_text[4], tweets_date[4], is_bot ]
        data_to_add = pandas.DataFrame([new_row], columns = myColumns)
        new_data = new_data.append(data_to_add)
    except Exception as e: #account probably banned
        print("BROKE--------------------------","index:", index)
        print(e)  
        
        pass
dataHandler.makeCSV(new_data, 100000)
