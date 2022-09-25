#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username, password = (argv[1], argv[2])
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(r.json().get('id'))
