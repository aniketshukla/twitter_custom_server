from twitter import Api



class Twitter(Api):

    '''Extends twitter api to capture tweets with retweet count >=0

    Streaming API could be used but the request session sometimes exceeds 2 minutes
       aborintg the entire functionality

     Tweet search retrieves tweets on the basis of hashtags
    '''

    def __init__(self,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,
                ACCESS_TOKEN_SECRET):
                self.api=Api(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,
                                        ACCESS_TOKEN_SECRET)



    def get_tweets(self):
        '''gets tweet from homefeed'''

        filtered_tweets=[]
        home_timeline=self.api.GetHomeTimeline(count=200)
        for tweet in home_timeline:
            if tweet.retweet_count>0:
                filtered_tweets.append(tweet.AsDict())
        return filtered_tweets



    def tweet_search(self,hashtag):
        '''gets tweet from search api'''

        return [sample.AsDict() for sample in self.api.GetSearch(term=hashtag)]
