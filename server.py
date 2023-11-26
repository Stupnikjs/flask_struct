from flask import Flask
from sqlalchemy import create_engine, URL, MetaData
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request


# pip install -r requirements.txt
app = Flask(__name__)


from router import *

# Creating the database URL
# uri = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

uri=os.getenv('DB_URI')

metadata = MetaData()

engine = create_engine(uri)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.getenv('PORT'))
