from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import argparse
import os
import psycopg2
import psycopg2.extras

class DBApi(Api):
    pass

class Home(Resource):
    def get(self):
        return "CS316FinalProject"

def run_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    api = DBApi(app)

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, required=True)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.p, debug=True)

if __name__ == '__main__':
    run_app()
