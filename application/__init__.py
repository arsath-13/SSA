from flask import Flask
from flask_pymongo import PyMongo

from securefiles import secretkey

app = Flask(__name__)
app.config["SECRET_KEY"] = secretkey.SECRET_KEY
app.config["MONGO_URI"] = secretkey.MONGO_URI

mongodb_client = PyMongo(app)
db = mongodb_client.db



from application import routes
