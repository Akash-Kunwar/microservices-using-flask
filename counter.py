from flask import Flask
from flask import request
from logger import root

count={}


app = Flask(__name__)


@app.route('/count',methods=['GET'])
def count():
    global count
    url=request.args.get('url')
    root.info('Calculating count for url{}'
              'status processing'.format(url))
    if url not in count:
        count[url]=1
    else:
        count[url]+=1
    root.info('Calculating count for url{}'
              'status Successfull'
              'Result {}'.format(url,count))
    return count[url]



if __name__ == '__main__':
    app.run(port='5002',debug=True)
