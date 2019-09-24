from flask import Flask
from flask import request

import jwt
import time
import sys

import requests

app = Flask(__name__)

counter_url = 'http://localhost:5004/counter'
timer_url = 'http://localhost:5003/timer'

count_timer = {}

jwt_secret = 'secret'

@app.route("/record", methods=['GET'])
def recorder():
    global counter_url, timer_url, count_timer
    token = request.args.get('access_token')
    token_payload = jwt.decode(token, jwt_secret, algorithm='HS256')

    if 'w' not in token_payload['perms']:
        return {'error_code': 'access_denied', 'message': 'The requested access is not allowed to perform the operation'}, 403

    url = request.args.get('url')
    payload = {'url': request.args.get('url')}
    count_response = requests.get(counter_url, params=payload)
    timer_response = requests.get(timer_url, params=payload)
    count_timer[url] = {'count': count_response.json().get(url), 'time': timer_response.json().get(url)}   
    return {'status': 'recorded'}, 200


@app.route("/retrieve", methods=['GET'])
def fetch_count_timer():
    global count_timer

    url = request.args.get('url')
    token = request.args.get('access_token')
    token_payload = jwt.decode(token, jwt_secret, algorithm='HS256')
    
    if 'r' not in token_payload['perms']:
        return {'error_code': 'access_denied', 'message': 'The requested access is not allowed to perform the operation'}, 403

    return count_timer[url]

if __name__ == "__main__":
    app.run('0.0.0.0', sys.argv[1])
    

