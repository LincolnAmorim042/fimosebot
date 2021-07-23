import tweepy
import time

#python -m setup.py


auth = tweepy.OAuthHandler('token','token')
auth.set_access_token('token-token','token')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'fimose'
nt = 500

for tweet in tweepy.Cursor(api.search, search).items(nt):
    try:
        tweet.retweet()
        print('Tweet Retweeted')
        time.sleep(900)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
