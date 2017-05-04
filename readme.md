# twitter


This project can perform the following functionality.

  - On opening route /cutserv , all tweets with #cutserv will be visible along with their other twitter data
  - On opening route /popular_tweets , all tweets fetched from timeline and having atleast a single retweet would be displayed
  - On opening route /cutserv/text , all tweets with #cutserv will be visible
  - On opening route /popular_tweets/text , all tweets with #cutserv will be visible
  - **Note** - This is a json endpoint with content-type json . To enable other content-type , server.Handler.response_handler(response_type="") for sending html documents. 


### Installation

This app requires [python](https://www.python.org/downloads/) v2.7 .

Install the dependencies and start the server.

```sh
pip install -r requirements.txt
```

To view the requirements
```sh
Your_favourite_text_editor requirements.txt
```

After installation finishes,run the main.py file

```sh
python main.py
```


### Adding your own functionality

The requirements of this project are minimal , _hence using a full blown server and web framework is not required_.

The module server extends the simple BaseHTTPRequestHandler and adds basic functionality like handling a get request.

Adding your own route
```python
from server.web_server import Server,router

@router('/yourroute')
def index():
    return json result
#note router is only used to return json or text based results as the content type is application/json
```

The following extends server to handle post request

```python
#add this method to server.web_server.handler to handle post request as well
def do_POST(self):
    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers.getheader('content-length'))
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
```

To listen on a different port
```python
#listens on post 8000
server.web_server.run_server(PORT=8000)
```

The module tweet.twit contains class Twitter which extends class twitter.Api from module python-twitter
Object methods get_tweets and tweet_search extend GetHomeTimeline() to get tweets with retweets atleast 1 and GetSearch() to get tweets with a particular hashtag

Read the documentation on [python-twitter](https://github.com/bear/python-twitter) to add your own functionality

```python
from tweet.twit import Twitter

twitter=Twitter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,
              ACCESS_TOKEN_SECRET)
result=twitter.tweet_search('#cutserv')
```

### Module documentation

**server**

```python
#add your own handler to server
server.web_server.Server(handler=handler_class)
Server.run_server(post=post_no)

#adding your own routes using decorator
def router(path):
    '''decorator to add new routes
    avoiding @wraps() here'''
    def router_method(func):
        print(__name__)
        path_to_function[path]=func
        return func
    return router_method

@route('/path')
def your_response_function():
  return json_doc
```

**twit**
```python
#creates an instance object and authorises the keys
twitter_object=tweet.twit.Twitter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,
              ACCESS_TOKEN_SECRET)

#get tweets with a like greater than 1 and returns them in the form of dictionary
twitter_object.get_tweets()

#search hashtags and other query terms
twitter_object.tweet_search(hashtag="#cutserv")

```
