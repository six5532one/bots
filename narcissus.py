import tweepy
import json

from tweepy.streaming import StreamListener
from tweepy.error import TweepError

# read credentials from disk
cred_file = "tweepy_demo_credentials.json"
with open(cred_file, 'rb') as f:
    credentials = json.loads(f.read())

CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']
ACCESS_TOKEN = credentials['access_token']
ACCESS_TOKEN_SECRET = credentials['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):
    def on_status(self, status):
        try: 
            self.api.retweet(status.id)
        except TweepError:
            pass

stream_listener = StdOutListener(api)
stream = tweepy.Stream(auth, stream_listener)
stream.filter(track=['@NarcissusFTW'])
