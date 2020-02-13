import tweepy
import csv
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
def get_all_tweets(screen_name):
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		# print("getting tweets before %s" % (oldest))
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		# print("...%s tweets downloaded so far" % (len(alltweets)))
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	pass

def followers(screen_name):
    allfollowers =[]
    followers = api.followers(screen_name = screen_name,count=200)
    allfollowers.extend(followers)
    for i in range(0,len(allfollowers)):
        print(allfollowers[i].name)

followers("Pratikanurag")
