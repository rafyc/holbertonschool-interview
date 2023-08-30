#!/usr/bin/python3
"""This module defines the count_words function"""
import requests


def count_words(subreddit, word_list, word_dict={}, after=""):
    """This method requests the api reddit to return the number time that
    a word is counted in the title of all article for a given subreddit"""

if not word_dict:
    word_dict = {key: 0 for key in word_list}

user_agent = "Pleasant_Situation20"
url = f'https://www.reddit.com/r/{subreddit}/hot.json'
headers = {'User-Agent': user_agent}
params = {'after': after, 'limit': 100}

req = requests.get(url, headers=headers, params=params, allow_redirects=False)

data = req.json().get('data')
after = data.get('after')

for ele in data.get('children', []):
    article_data = ele.get('data', {})
    title = article_data.get('title', '').lower()
    for word in word_list:
        if (word in title):
            word_dict[word] += 1
            if after is not None:
                return count_words(subreddit, word_list, word_dict, after)
sorted_wordDict = dict(sorted(word_dict.items()))
for key, value in sorted_wordDict.items():
    if (value != 0):
        print(f"{key}: {value}")

return sorted_wordDict
