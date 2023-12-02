from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from model import Base
import os

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.after_request
def addCors(response):
    allowed_origins = ['https://remplasveltenew.fly.dev']
    origin = request.headers.get('Origin')
    
    if origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Credentials'] = 'true'  # Enable if you're using credentials (cookies, HTTP authentication)

    return response

from router import *


uri = ''

if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']

if uri == '':
    uri = 'postgresql://lziqbjkd:HP_7F8AFjzdQO8vXtVPrEJLV0wRRcML2@dumbo.db.elephantsql.com:5432/lziqbjkd'



engine = create_engine(uri)




Base.metadata.create_all(engine, checkfirst=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.environ.get('PORT'))
