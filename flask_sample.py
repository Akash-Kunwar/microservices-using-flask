from flask import Flask
import time

import requests

app = Flask(__name__)

count = 0

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/counter")
def counter():
    global count
    count += 1
    return "The app has been invoked {} times".format(count)

@app.route("/timer")
def timer():
    start_time = time.time() * 1000
    requests.get('https://httpstat.us/200')
    end_time = time.time() * 1000
    return 'Time required to make the http call {}'.format(end_time - start_time)

if __name__ == "__main__":
    app.run('0.0.0.0', '5003')

