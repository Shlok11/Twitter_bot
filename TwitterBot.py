import tweepy
import time


print("This is twitter bot", flush=True)

CONSUMER_KEY = 'SpquNaWHTFRrrV4p94QisSwtt'
CONSUMER_SECRET = 'EOsApHAO4l2eTeXrKFmu7i4zGLs7vgJJMW3c9JQcHShnvpRYH7'
ACCESS_KEY = '963288418754093056-m4FqV6psAoB9pSmuh9QMPD2O3WkPcFX'
ACCESS_SECRET = 'WNxno2MhHtcjt01UDOocFUmHWgYTVDu6BBAIPnDjLZk5V'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_tweets():
    print('Retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')

    for mention in mentions:
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if '#hellotwitter' in mention.text.lower():
            print('Found #hellotwitter')
            print('Responding back....')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld Back to you!', mention.id)

while True:
    reply_tweets()
    time.sleep(15)
