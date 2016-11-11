from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import argparse
import os
import psycopg2
import psycopg2.extras
from rest_models import DBUtil, District, Position, Speaker, Speech, SpeechAssociation, Users

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

    dbutil = DBUtil()
    api.add_resource(District, '/district', resource_class_args=(dbutil,))
    api.add_resource(Position, '/position', resource_class_args=(dbutil,))
    api.add_resource(Speaker, '/speaker', resource_class_args=(dbutil,))
    api.add_resource(Speech, '/speech', resource_class_args=(dbutil,))
    api.add_resource(SpeechAssociation, '/speechassociation', resource_class_args=(dbutil,))
    api.add_resource(Users, '/users', resource_class_args=(dbutil,))

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, required=True)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.p, debug=True)

if __name__ == '__main__':
    run_app()
