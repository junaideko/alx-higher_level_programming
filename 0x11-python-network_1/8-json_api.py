#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    var = "" if len(argv) == 1 else argv[1]
    r = requests.post(url, data={'q': var})
    try:
        dic = r.json()
        if dic:
            print(f"[{dic.get('id')}] {dic.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
