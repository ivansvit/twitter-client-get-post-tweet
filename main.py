import tweepy
import os
from datetime import datetime, timedelta
import pytz

# -------------------------------------- VARIABLES --------------------------------------

API_KEY = os.environ.get("API_KEY")
API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# -------------------------------------- CLIENTS --------------------------------------

# Create a client to read tweets with our parameters
client = tweepy.Client(bearer_token=BEARER_TOKEN)
# Create a client to post a tweet
client_post = tweepy.Client(consumer_key=API_KEY,
                            consumer_secret=API_KEY_SECRET,
                            access_token=ACCESS_TOKEN,
                            access_token_secret=ACCESS_TOKEN_SECRET)

# -------------------------------------- FUNCTIONS --------------------------------------

# Function to get a tweet by id
def get_tweet_by_id(tweet_id):
    tweet = client.get_tweet(id=tweet_id)
    print(tweet)

# Function to create tweet by enter text
def create_tweet(tweet_text):
    response = client_post.create_tweet(text=tweet_text)
    print(response)

# Function that allows us to find tweets by keyword for the last day
def get_tweets_by_keyword(keyword):
    search_params = f"{keyword} -is:retweet"
    response = client.search_recent_tweets(query=search_params,
                                           tweet_fields=["created_at", "lang"],
                                           max_results=100,
                                           expansions=["author_id"])
    data = response.data

    # Last 24 hours. It serves to search tweets from last 24h
    now = datetime.now()
    # Make current datetime aware of the timezone with pytz
    now = pytz.utc.localize(now)
    one_day_back = now - timedelta(days=1)
    # Create list of languages for sort tweets we can understand
    list_lang = ["it", "en"]

    # Check if there is data for keyword given within last 24h.
    if data:
        for tweet in data:
            # If statement to check the date and time of each tweet from the data. If within 24h print
            if tweet.created_at > one_day_back and tweet.lang in list_lang:
                print(tweet.id)
                print(tweet.text)
                print(tweet.created_at)
                print(tweet.lang)
                print(tweet.author_id)
    else:
        print("No tweets with that keyword in the last 24 hours.")

# -------------------------------------- TEST CODE --------------------------------------

# Call the function
get_tweet_by_id(tweet_id="1490336052627841025")
get_tweets_by_keyword(keyword="Florence")