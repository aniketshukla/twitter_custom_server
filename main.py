'''
root file of the project
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
    '''returns tweets with hashtag #cutserv'''
    #return json.dumps(twitter.tweet_search('#cutserv'))
    result=[]
    for tweet in twitter.tweet_search('#cutserv'):
        try:
            tweet[u'user'][u'screen_name']=tweet[u'user'][u'screen_name'].decode('utf-8').encode('utf-8')
            result.append(tweet)
        except Exception as err:
            1



    return Server.render('index.html',data=result,title="#cutserv")



@router('/cutserv')
def hashtag():
    '''returns tweets with hashtag #cutserv'''
    #return json.dumps(twitter.tweet_search('#cutserv'))
    result=[]
    for tweet in twitter.tweet_search('#cutserv'):
        '''Jinja template requires the data to be in UTF-8 format and some of the data sent by twitter
        is not in UTF-8 format ,hence decoding and encoding it again sometimes fixes the problem'''
        try:
            tweet[u'user'][u'screen_name']=tweet[u'user'][u'screen_name'].decode('utf-8').encode('utf-8')
            tweet[u'text']=tweet[u'text'].decode('utf-8').encode('utf-8')
            try:
                tweet[u'user'][u'retweeted_status'][u'user'][u'screen_name']=tweet[u'user'][u'retweeted_status'][u'user'][u'screen_name'].decode('utf-8').encode('utf-8')
            except Exception as err:
                1
            result.append(tweet)
        except Exception as err:
            1



    return Server.render('tweets.html',data=result,title="#cutserv")



@router('/popular_tweets')
def popular_tweets():
    '''returns tweets with atleast a single retweet'''
    result=[]
    for tweet in twitter.get_tweets():
        '''Jinja template requires the data to be in UTF-8 format and some of the data sent by twitter
        is not in UTF-8 format ,hence decoding and encoding it again sometimes fixes the problem'''
        try:
            tweet[u'user'][u'screen_name']=tweet[u'user'][u'screen_name'].decode('utf-8').encode('utf-8')
            tweet[u'text']=tweet[u'text'].decode('utf-8').encode('utf-8')
            try:
                tweet[u'user'][u'retweeted_status'][u'user'][u'screen_name']=tweet[u'user'][u'retweeted_status'][u'user'][u'screen_name'].decode('utf-8').encode('utf-8')
            except Exception as err:
                1
            result.append(tweet)
        except Exception as err:
            1
    return Server.render('tweets.html',data=result,title="Popular Tweets")



if __name__=='__main__':
    server=Server()
    server.run_server()
