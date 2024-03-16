from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)

# This code does not work, it grabs the string proeply but fials to connect as excpected
#print(app.config.get('MONGO_URI'))  # Should be None or the default value
#app.config.from_pyfile('config.py', silent=True)  
#print(app.config.get('MONGO_URI'))  # Should now show the URI from config.py

#Alternative approch
app.config["MONGO_URI"] = "mongodb+srv://hesho:YNLu3qGf1s2kyyp7@fawakihdb.acooj0o.mongodb.net/testDB?retryWrites=true&w=majority"

# Ensure MONGO_URI is present
if not app.config.get('MONGO_URI'):
    raise ValueError("MONGO_URI is not set in the configuration.")

# Initialize PyMongo
mongo = PyMongo(app)

# Import routes
from app.routes import route
