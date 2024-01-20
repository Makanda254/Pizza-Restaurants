#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import Restaurant, RestaurantPizza, Pizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app)

db.init_app(app)

api = Api(app)

class Index(Resource):
    
    def get(self):
         
         response_dict={
             "message":"Welcome to Restaurant domain API"
         }
        
         return make_response(
             jsonify(response_dict),
             200
         )
    
api.add_resource(Index, '/')





if __name__ == '__main__':
    app.run(port=5555, debug=True)
    


