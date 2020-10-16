from flask_restful import Resource
from flask import Response, jsonify
from chatbot_api.food.food_dao import FoodDao

class OrderApi(Resource):
    def __init__(self):
        self.dao = FoodDao()
