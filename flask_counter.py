from flask import Flask
from flask import request

import sys

import time

import requests

app = Flask(__name__)

counter = {}

@app.route("/counter", methods=['GET'])
def count():
    global counter
    url = request.args.get('url')
    if not url in counter:
        counter[url] = 1
    else:
        counter[url]+=1
    return {url: counter[url]}

if __name__ == "__main__":
    app.run('0.0.0.0', sys.argv[1])

