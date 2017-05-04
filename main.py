'''root file of the project
uses module tweet and server
tweet -> getting twitter samples for homefeed and searches tweet on the basis of hashtag
server -> is a basic instance of basicHTTPserver nad extends to make serving get request easier
'''

import sys
from server.web_server import Server,router
from tweet.twit import Twitter
import json



twitter=Twitter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,
              ACCESS_TOKEN_SECRET)



@router('/')
def main():
    return ('{err:working}')



@router('/cutserv')
def hashtag():
    '''returns tweets with hashtag #cutserv'''
    return json.dumps(twitter.tweet_search('#cutserv'))



@router('/cutserv/text')
def hashtag_text():
    '''returns just the text of tweets with hashtag #cutserv'''
    return json.dumps([tweet_text['text'] for tweet_text in twitter.tweet_search('#cutserv')])



@router('/popular_tweets')
def popular_tweets():
    '''returns tweets with atleast a single retweet'''
    return json.dumps(twitter.get_tweets())



@router('/popular_tweets/text')
def popular_tweets_text():
    '''returns text of tweets with atleast a singel retweet'''
    return json.dumps([tweet_text['text'] for tweet_text in twitter.get_tweets()])



@router('/')
def index():
    '''a summar of the entire application '''
    return '''open /popular_tweets for complete tweet information of tweets with like greater than 1 , /popular_tweets/text for text of tweets with like greater than 1 ,/cutserv for complete tweet info of tweets with hashtag cutserv, and /cutserv/text for tweets with hashtag cutserv'''



if __name__=='__main__':
    server=Server()
    server.run_server()
