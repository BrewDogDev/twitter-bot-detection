import dataHandler


import re
from strsimpy.levenshtein import Levenshtein
levenshtein = Levenshtein()

import pandas

def contains_bot(string):
    return "bot" in string
def calcLevenstein(str1, str2):
    return levenshtein.distance(str1, str2)
def contains_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    links = re.findall(regex, string)
    return len(links)>0
def is_retweet(string):
    return string[:2] == "RT"
def num_tweets_contain_link(strList):
    count = 0
    for string in strList:
        if contains_link(string):
            count = count + 1
    return count
def num_tweets_contain_bot(strList):
    count = 0
    for string in strList:
        if contains_bot(string):
            count = count + 1
    return count
def num_retweets(strList):
    count = 0
    for string in strList:
        if is_retweet(string):
            count = count + 1
    return count



dataFile = "data/twitter_data.csv"
old_data = dataHandler.getDataFrame(dataFile)

print(old_data.shape)

features = [
    "name_contains_bot",
    "screen_name_contains_bot",
    "name_screen_levenshtein",
    "followers_count",
    "following_count",
    "favorites_count",
    "tweets_count",
    "verified",
    "location",
    "description_contains_link",
    "description_contains_bot",
    "tweets_contains_link_count",
    "tweets_contains_bot_count",
    "retweet_count",
    "tweet_levenstein1",
    "tweet_levenstein2",
    "tweet_levenstein3",
    "tweet_levenstein4",
    "is_bot"
]

new_data = pandas.DataFrame(columns=features)

for index, user in old_data.iterrows():
    print(index)
    try:
        new_row = [
            contains_bot(user["name"]),
            contains_bot(user["screen_name"]),
            calcLevenstein(user["name"], user["screen_name"]),
            user["followers_count"],
            user["following_count"],
            user["favorites_count"],
            user["tweets_count"],
            user["verified"],
            user["Location"],
            contains_link(user["description"]),
            contains_bot(user["description"]),
            num_tweets_contain_link([user["tweet1_text"], user["tweet2_text"], user["tweet3_text"], user["tweet4_text"], user["tweet5_text"]]),
            num_tweets_contain_bot([user["tweet1_text"], user["tweet2_text"], user["tweet3_text"], user["tweet4_text"], user["tweet5_text"]]),
            num_retweets([user["tweet1_text"], user["tweet2_text"], user["tweet3_text"], user["tweet4_text"], user["tweet5_text"],]),
            calcLevenstein(user["tweet1_text"], user["tweet2_text"]),
            calcLevenstein(user["tweet1_text"], user["tweet3_text"]),
            calcLevenstein(user["tweet1_text"], user["tweet4_text"]),
            calcLevenstein(user["tweet1_text"], user["tweet5_text"]),
            user["is_bot"]
        ]
        data_to_add = pandas.DataFrame([new_row], columns = features)
        new_data = new_data.append(data_to_add)
    except Exception as e:
        print("Broke", e)

print(new_data.shape)

dataHandler.makeCSV(new_data, 420420)



