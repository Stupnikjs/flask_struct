from flask import Flask
from sqlalchemy import create_engine, URL, MetaData
import os


from flask import Flask, jsonify, request


app = Flask(__name__)


from router import *


uri=os.environ['DB_URI']


metadata = MetaData()

engine = create_engine(uri)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.environ.get('PORT'))
