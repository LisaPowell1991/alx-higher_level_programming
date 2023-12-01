#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request


url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

    print("Body response:")
    print("   - type", type(body))
    print("   - content:", body)
    print("   - utf8 content:", body.decode('utf-8'))
