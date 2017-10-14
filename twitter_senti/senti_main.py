import tweepy
from googletrans import Translator
import textblob as tb
import json

c_key = "lEfKUknEK3cqlzOuamilKdCC8"
c_sec = "MFd4NsWqISUCtWMZoH5IxsU6mHz22SfvxVn8PhrOSwaxn2bFq3"

a_tok = "98061773-VFd6f0DddBNpylXXWamdTCptdwlxREZ4TcQecClWH"
a_tok_sec = "phO8TduXACCTpHONCKbyxuU3Ng6MDe0rvSUe7GwhFt9Vi"

auth = tweepy.OAuthHandler(c_key, c_sec)
auth.set_access_token(a_tok, a_tok_sec)

api = tweepy.API(auth)

public_tweets = api.search(q='biggboss', count=100)
print(len(public_tweets))
translator = Translator()
for tweet in public_tweets:
    if 'RT' not in tweet.text:
        try:
            eng_tweet = translator.translate(str(tweet.text), dest='en')
            print(eng_tweet.text)
            analysis = tb.TextBlob(eng_tweet.text)
            print(analysis.sentiment)
        except json.decoder.JSONDecodeError:
            pass

    else:
        print('retweet')