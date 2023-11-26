from flask import Flask
from sqlalchemy import create_engine, URL, MetaData
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request


# pip install -r requirements.txt
app = Flask(__name__)


from router import *

# Assuming you have the environment variables set
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_USER")

# Creating the database URL
uri = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

print(uri)
metadata = MetaData()

engine = create_engine(uri)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.getenv('PORT'))
