#!/usr/bin/python3
"""Function to retrive hot posts on a specific subreddit."""
import requests


def top_ten(subreddit):
    """Print the top 10 hottest titles in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(t.get("data").get("title")) for t in results.get("children")]
