from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_pyfile('config.py', silent=True)

# Ensure MONGO_URI is present
if not app.config.get('MONGO_URI'):
    raise ValueError("MONGO_URI is not set in the configuration.")

# Initialize PyMongo
mongo = PyMongo(app)


# Import routes
from app.routes import route
