from flask import Flask
from flask import request

import time
import sys


app = Flask(__name__)

count = 0

@app.route("/timer", methods=['GET'])
def timer():
    url = request.args.get('url')
    start_time = time.time() * 1000
    request.get(url)
    end_time = time.time() * 1000
    return {url: end_time - start_time}, 200

if __name__ == "__main__":
    app.run('0.0.0.0', '5003')

