from flask import Flask
from flask import request
import jwt

import time
import sys

import requests

app = Flask(__name__)

count = 0
jwt_key = 'secret'

@app.route("/request_access", methods=['GET'])
def access():
    global jwt_key

    url = request.args.get('url')
    perms = request.args.get('perms')

    payload = {'requested_url': url, 'perms': perms, 'exp': int(time.time() * 1000 + 60 * 1000)}
    token = jwt.encode(payload, jwt_key, algorithm='HS256')
    return {url: token}, 200

if __name__ == "__main__":
    app.run('0.0.0.0', sys.argv[1])

