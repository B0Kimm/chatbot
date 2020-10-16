from flask_restful import Resource
from flask import Response, jsonify
from chatbot_api.order.order_dao import OrderDao

class OrderApi(Resource):
    def __init__(self):
        self.dao = OrderDao()
