from flask import Flask
from sqlalchemy import create_engine, URL, MetaData
import os


from flask import Flask, jsonify, request, make_response


app = Flask(__name__)


from router import *

uri = ''

if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']

if uri == '':
    uri = 'postgresql://lziqbjkd:HP_7F8AFjzdQO8vXtVPrEJLV0wRRcML2@dumbo.db.elephantsql.com:5432/lziqbjkd'


metadata = MetaData()

engine = create_engine(uri)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.environ.get('PORT'))
