#!/usr/bin/python3
"""This module defines the count_words function for counting word occurrences
in Reddit titles."""
import requests


def count_words(subreddit, word_list, word_dict={}, after=""):
"""Count the occurrences of specified words in the titles of Reddit articles.

Args:
subreddit (str): The name of the subreddit.
word_list (list): A list of words to count occurrences for.
word_dict (dict, optional): A dictionary to store word occurrences. Default is
an empty dictionary.
after (str, optional): Pagination token for Reddit API. Default is an empty
string.

Returns:
dict: A dictionary containing word occurrences.

"""
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
