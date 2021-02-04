#!/usr/bin/python3
""" recursive program to get alllhot  posts from a subreddit
    using the reddit api
"""
import requests
from sys import argv


def do_request(subreddit, after):
    """ Do request to endopoint"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=50&after={}'
    userA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
            Gecko/20100101 Firefox/76.0"

    hdr = {"User-Agent": userA}
    response = requests.get(url.format(subreddit, after), headers=hdr)
    return response


def recurse(subreddit, hot_list=[], after=''):
    """ do recursion while there are a next page of
        posts
    """
    res = do_request(subreddit, after)
    if res.status_code != 200:
        return None

    res = res.json()
    after = res['data']['after']
    for post in res['data']['children']:
        hot_list.append(post['data']['title'])

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
