from application import app

if __name__ == "__main__":
    app.run(debug = True)

# from flask import Flask, render_template, url_for
# from pymongo import MongoClient
#
# app = Flask(__name__)
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['SmartSalesAutomation']
#
#
# if __name__ == "__main__":
#     app.run(debug=True)