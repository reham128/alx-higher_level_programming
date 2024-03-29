#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    req = requests.get(url)
    commit = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(commit[i].get("sha"),
                  commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
