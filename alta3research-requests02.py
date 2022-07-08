#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/hint"

new_hero = {
    "name": "Ronald McDonald",
    "realName": "REDACTED",
    "since": 1934,
    "powers": ["Is a Clown", "Can Join Forces with the Hamburglar and Grimace", "Can cause enemies' arteries to be clogged at a moments notice"]
}

# json.dumps takes a python object and returns it as a JSON string
new_hero = json.dumps(new_hero)

# requests.post requires two arguments at the minimum;
# a url to send the request
# and a json string to attach to the request
resp = requests.post(URL, json=new_hero)

# pretty-print the response back from our POST request
pprint(resp.json())
