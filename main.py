'''root file of the project
uses module tweet and server
tweet -> getting twitter samples for homefeed and searches tweet on the basis of hashtag
server -> is a basic instance of basicHTTPserver nad extends to make serving get request easier
'''

import sys
from server.web_server import Server,router
from tweet.twit import Twitter
import json



twitter=Twitter('P3BGrlY3uKzwhqU7XDWRmDKpZ',
            'J4EykDvFHi6DVVRzwdJRX95z6YZCKGXxTkDbR3048vJpnEmLiP',
            '1026811693-fhGTpNENexbs8MrFSycrKX2ti8SNfbhynG29Ii7',
            'tfO1t2ePcG45GqCmDYsn6vIXOwwLgRODze5NMTEyItpNE')



@router('/')
def main():
    return ('{err:working}')



@router('/cutserv')
def hashtag():
    return json.dumps(twitter.tweet_search('#cutserv'))



@router('/cutserv/text')
def hashtag_text():
    return json.dumps([tweet_text['text'] for tweet_text in twitter.tweet_search('#cutserv')])



@router('/popular_tweets')
def popular_tweets():
    return json.dumps(twitter.get_tweets())



@router('/popular_tweets/text')
def popular_tweets_text():
    return json.dumps([tweet_text['text'] for tweet_text in twitter.get_tweets()])



@router('/')
def index():
    return '''open /popular_tweets for complete tweet information of tweets with like greater than 1 , /popular_tweets/text for text of tweets with like greater than 1 ,/cutserv for complete tweet info of tweets with hashtag cutserv, and /cutserv/text for tweets with hashtag cutserv'''



if __name__=='__main__':
    server=Server()
    server.run_server()
