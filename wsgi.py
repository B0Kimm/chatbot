from flask import Flask, jsonify
from flask_restful import Api
from chatbot_api.routes import initialize_routes

app = Flask(__name__)
api = Api(app)


initialize_routes(api)