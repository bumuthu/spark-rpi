  
from flask import Flask
from flask_restful import Resource, Api
import controller


app = Flask(__name__)
api = Api(app)
api.add_resource(controller.Controller, '/api/object-count')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)