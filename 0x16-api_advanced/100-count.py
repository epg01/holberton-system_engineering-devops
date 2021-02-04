#!/usr/bin/python3

import operator
import requests

def do_request(subreddit, after):
    """ Do request to endopoint"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
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


def count_words(subreddit, word_list, i=0, hot_list=[], res={}):
    
    after = ''
    subs = word_list[i].split(',')[0]
    patterns = []
    if len(hot_list) == 0:
        hot_list = recurse(subreddit, hot_list, after)

    for el in hot_list:
        split_line = el.split(' ')
        for w in split_line:
            if subs == w or subs.capitalize() == w:
                patterns.append(w)

    res[subs] = len(patterns)
    i += 1
    
    if i != len(word_list):
        count_words(subreddit, word_list, i, hot_list, res)
    else:
        sort_res = {}
        sort_res = dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True))
        for k,v in  sort_res.items():
            if v > 0:
                print('{}: {}'.format(k, v))
