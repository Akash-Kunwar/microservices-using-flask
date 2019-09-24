from flask import Flask
from flask import request
from logger import root
import time
import requests

'''url=request.args.get('url')
root.info('Calculating time  for url {} status processing'.format(url))
s_time=time.time()*1000
requests.get(url)
e_time=time.time()*1000
root.info('Calculating count for url {} status Successfull Time:{}'.format(url,e_time-s_time))
x=str(e_time-s_time)
return x
'''
app = Flask(__name__)

@app.route('/timer',methods=['GET'])
def timer():
    url=request.args.get('url')
    root.info('Calculating time  for url {} status processing'.format(url))
    s_time=time.time()*1000
    requests.get(url)
    e_time=time.time()*1000
    root.info('Calculating count for url {} status Successfull Time:{}'.format(url,e_time-s_time))
    return str(e_time-s_time)



if __name__ == '__main__':
    app.run(port='5003',debug=True)
