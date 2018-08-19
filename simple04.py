from dotenv import load_dotenv
# load_dotenv()
load_dotenv(verbose=True)

import os
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    # curl http://127.0.0.1:5000/
    def get(self):
        return {"about": "Hello World!"}

    # curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"test":"Hello"}'
    def post(self):
        some_json = request.get_json()
        return {"some_json": some_json}, 201


class Multi(Resource):

    # curl http://127.0.0.1:5000/multi/10
    def get(self, num):
        return {"result": num*10}


api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)
