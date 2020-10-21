#import necessary libraries
from flask import Flask
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from google.cloud import bigquery
from flask_cors import CORS
import os

# import otherroute! which is another py file

# try:
#     # The typical way to import flask-cors
#     from flask.cor import cross_origin
# except ImportError:
#     # Path hack allows examples to be run without installation.
#     import os
#     parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.sys.path.insert(0, parentdir)

#     from flask.cors import cross_origin



#create Flask app instance
app = Flask(__name__)
cors=CORS(app, resources=r'smallSst.json', allow_headers='Content-Type')

@app.route("/",methods=['GET'])
# @cross_origin()
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port = 1123)