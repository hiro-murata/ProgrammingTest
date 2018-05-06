from requests_oauthlib import OAuth1
import requests
import urllib

CONSUMER_KEY = "UhuBsj54DbRnnHGQYaPywHmAi"
CONSUMER_SECRET = "e1zSaGoQorVKzyW5W7U8LaAmkUsf3nnjdIHCxh45Y03bnnBj86"
ACCESS_TOKEN = "42566916-5CI2BDtmiUQdWFKtTY6ajgxmLlYjURI4ftW2K88h3"
ACCESS_TOKEN_SECRET = "YHfdFB1RJxIcHQ6XOriX0GZhmZmFpNmI5wegaBIRDflIU"
url = "https://api.twitter.com/1.1/search/tweets.json?count=10&lang=ja&q=" + urllib.parse.quote_plus("JustinBieber")
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
answers = requests.get(url, auth = auth)
tweets = answers.json()['statuses']
for tweet in tweets:
    print('')
    print(tweet["text"])
    print('')
