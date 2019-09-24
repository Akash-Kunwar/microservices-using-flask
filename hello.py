from flask import Flask
from flask import request
import requests
import time
import jwt

app = Flask(__name__)
jwt_key='bnmit_secret'

count=0



@app.route('/count',methods=['GET'])
def count():
    global count
    count=count+1
    return 'number :{}'.format(count)



@app.route('/timer',methods=['GET'])
def timer():
	url=request.args.get('url')
	s_time=time.time()*1000
	requests.get(url)
	e_time=time.time()*1000
	return 'time to request {} is {}'.format(url,e_time-s_time)



@app.route('/echo',methods=['GET'])
def echo():
	name=request.args.get('name')
	return 'name ={}'.format(name)


@app.route('/fetch_access',methods=['GET'])
def fetch_access():
	url=request.args.get('url')
	perm=request.args.get('perm')
	payload={
	'url' : url,
	'perm' : perm
	}
	token=jwt.encode(payload,jwt_key,algorithm='HS256')
	return token


@app.route('/check_access',methods=['GET'])
def check_access():
    token=request.args.get('access_token')
    payload=jwt.decode(token,jwt_key)
    return payload




if __name__ == '__main__':
    app.run(port='5001',debug=True)
