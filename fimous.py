import tweepy
import time

#python -m setup.py


auth = tweepy.OAuthHandler('4nNJV75ZLujBrE3SDR6jYi3dH','S1vQa7zqg5ePqMpQVdLXdwewUJX5dGjsmrAONIkwuDhXlOJrJg')
auth.set_access_token('1267610070566699015-xpcj2UAHHHzH7aB2MeJPlUw0aChJjn','T8pysfjucC6m53P9hJ63MYCD9Fyn58Xe2lYzYwQYEjLkk')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'fimose'
nt = 500

for tweet in tweepy.Cursor(api.search, search).items(nt):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(900)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
