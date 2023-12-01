#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"{'  - type:'} {type(body)}")
        print(f"{'  - content:'} {body}")
        print(f"{'  - utf8 content:'} {body.decode('utf-8')}")
