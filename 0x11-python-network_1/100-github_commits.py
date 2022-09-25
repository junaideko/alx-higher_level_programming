#!/usr/bin/python3
"""Python script that lists 10 commits
(from the most recent to oldest) of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    json_list = r.json()
    for dic in json_list[:10]:
        print("{}: {}".format(dic.get('sha'),
                              dic.get('commit').get('author').get('name')))
