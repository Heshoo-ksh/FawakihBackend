from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
mongo = PyMongo(app)
