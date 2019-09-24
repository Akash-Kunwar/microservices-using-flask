from flask import Flask
from flask import request

import time
import sys

import requests

app = Flask(__name__)

counter_url = 'http://localhost:5004/counter'
timer_url = 'http://localhost:5003/timer'


count_timer = {}

@app.route("/count_timer", methods=['GET'])
def counter_timer():
    global counter_url, timer_url, count_timer
    url = request.args.get('url')
    payload = {'url': request.args.get('url')}
    count_response = requests.get(counter_url, params=payload)
    timer_response = requests.get(timer_url, params=payload)
    return {'count': count_response.json().get(url), 'time': timer_response.json().get(url)}

if __name__ == "__main__":
    app.run('0.0.0.0', sys.argv[1])
    

