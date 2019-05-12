import tweepy


# Defining API Access keys
# Twitter:
consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXXXX'
access_token_secret = 'XXXXXXXXXX'


# Authenticating to my account based on above keys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Check it's the right account by retrieving and printing username
user = api.me()
print(user.name)


# Main Function, holds main bot functions

def mainfunction():

    # Follows back all followers
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()

    # Searches for tweets with "Hearthstone and favorites them, max 10
    search = ('Hearthstone')
    number_of_tweets = 10
    for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
        try:
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)


    # Prints when the function is done, for troubleshooting
    print('Function Check')

# Call the function


mainfunction()


# Prints when the script is complete for troubleshooting
print('Jobs Done')
