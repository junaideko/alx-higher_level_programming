#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-IdX-Request-Id in the response header"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print("{}".format(r.headers.get("X-Request-Id")))
