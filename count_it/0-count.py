#!/usr/bin/python3
"""
This module defines the count_words function
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    This method requests the api reddit to return the number time that
    a word is counted in the title of all article for a given subreddit
    """
    word_list = [ele.lower() for ele in word_list]

    user_agent = "Pleasant_Situation20"
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': user_agent}
    count = 0
    wordDict = {key: 0 for key in word_list}
    req = requests.get(url, headers=headers, allow_redirects=False)
    data = req.json().get('data')
    for ele in data.get('children', []):
        article_data = ele.get('data', {})
        title = article_data.get('title', '').lower()
        for word in word_list:
            if(word in title):
                wordDict[word] += 1
    for key, value in wordDict.items():
        print(f"{key}: {value}")
