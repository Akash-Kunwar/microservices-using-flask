from flask import Flask
from flask import request
from logger import root
import jwt

app = Flask(__name__)
jwt_key='bnmit_secret'
user_access={
   "1":["https://google.com","https://facebook.com"],
   "2":["https://google.com"]
}
@app.route('/fetch_access',methods=['GET'])
def fetch_access():
	url=request.args.get('url')
	perm=request.args.get('perm')
    user_id=request.args.get('user_id')
    if url not in user_access[user_id]:
        return {'error ':'Invalid access'},403
    root.info('Creating  Token for url{}'
              'status: processing'.format(url))
	payload={
	'url' : url,
	'perm' : perm,
    'user_id':user_id}
	token=jwt.encode(payload,jwt_key,algorithm='HS256')
    root.info('Calculating Token for url{}'
              'status:Successfull'.format(url))
	return token
@app.route('/check_access',methods=['GET'])
def check_access():
    global user_access
    token=request.args.get('access_token')
    root.info('Decoding Token'
              'status processing')
    payload=jwt.decode(token,jwt_key)
    root.info('Decoding Token'
              'status Successfull')
    return payload
if __name__ == '__main__':
    app.run(port='5004',debug=True)
