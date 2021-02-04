#!/usr/bin/python3
"""
Get the hottest posts from a subreddit
limit = 0
"""
import requests
from sys import argv


def top_ten(subreddit):
    """ get data form reddit api"""

    query_st = 'limit=10'
    url = 'http://www.reddit.com/r/{}/hot.json?{}'.format(subreddit, query_st)
    userA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
            Gecko/20100101 Firefox/76.0"

    headers = {"User-Agent": userA}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        for post in response['data']['children']:
            print(post['data']['title'])
    else:
        return print('None')
