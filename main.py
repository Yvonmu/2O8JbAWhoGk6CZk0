import tweepy
import csv
import pandas as pd

access_token = ""
access_token_secret = ""
api_key = ""
api_key_secret = ""


def f_access():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    search_key = ""
    csv_file = open(search_key + ".csv", 'a+', newline='', encoding="utf-8")
    csvWriter = csv.writer(csv_file)
    c = []
    i = []
    u = []
    t = []
    for tweet in tweepy.Cursor(api.search, q=search_key, count=1000, lang='id', since='2021-07-05',
                               until='2021-07-08').items():
        print(tweet.created_at, tweet.id, tweet.user.name, tweet.text)
        c.append(tweet.created_at)
        i.append(tweet.id)
        u.append(tweet.user.name)
        t.append(tweet.text.encode('utf-8'))
        tweets = [tweet.created_at, tweet.id, tweet.user.name, tweet.text.encode('utf-8')]
        csvWriter.writerow(tweets)
    dictTweets = {"Date": c, 'id': i, 'username': u, 'text': t}
    df = pd.DataFrame(dictTweets, columns=['Date', 'id', 'username', 'txt'])
    df


if __name__ == '__main__':
    f_access()
