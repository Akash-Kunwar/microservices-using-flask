from flask import Flask
from flask import request
from logger import root
import requests



app = Flask(__name__)

access_provider_url='http://localhost:5004'
count_provider_url='http://localhost:5002'
timer_url='http://localhost:5003'

@app.route('/v1/access',methods=['GET'])
def access():
    global access_provider_url,count_provider_url,timer_url
    user_id=request.args.get('user_id')
    url=request.args.get('url')


    payload={
    'user_id':user_id,
    'url':url,
    'perm':'rw'
    }

    token=requests.get(access_provider_url+"/fetch_access",param=payload)

    if token.status_code==403:
        return {'error':'Invalid access'},403
    return token.text


@app.route("/v1/stream",methods=['GET'])
def stream():
    token=request.args.get('token')
    payload={
    'access_token':token
    }
    token=requests.get(access_provider_url+"/check_access",param=payload)
    token_decoded=token.json()

    url=token_decoded['url']
    vedio_content=request.get(url)
    return vedio_content.content,200

if __name__ == '__main__':
    app.run(port='5001',debug=True)
