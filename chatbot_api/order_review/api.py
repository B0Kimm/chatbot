from typing import List
from flask import request
from flask_restful import Resource, reqparse
from chatbot_api.order_review.dao import OrderReviewDao
from chatbot_api.order_review.dto import OrderReviewDto, OrderReviewVo
import json
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('order_id', type=int, required=True, help='This field should be a order_id')
parser.add_argument('order_time', type=str, required=True, help='This field should be a order_time')
parser.add_argument('review_cmnt', type=str, required=False, help='This field should be a review_cmnt')
parser.add_argument('taste_rate', type=float, required=False, help='This field should be a taste_rate')
parser.add_argument('quantity_rate', type=float, required=False, help='This field should be a quantity_rate')
parser.add_argument('delivery_rate', type=float, required=False, help='This field should be a delivery_rate')
parser.add_argument('review_time', type=str, required=False, help='This field should be a review_time')
parser.add_argument('review_img', type=str, required=False, help='This field should be a review_img')
parser.add_argument('owner_cmnt', type=str, required=False, help='This field should be a owner_cmnt')
parser.add_argument('userid', type=str, required=True, help='This field should be a userid')
parser.add_argument('shop_id', type=int, required=True, help='This field should be a shop_id')
parser.add_argument('food_id', type=int, required=True, help='This field should be a food_id')

class OrderReview(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        return {'message': 'Server Start'}

    @staticmethod
    def get(order_id):
        ...

    @staticmethod
    def update():
        ...

    @staticmethod
    def delete():
        ....

class Users(Resource):
    def post(self):
        ...

    def get(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...

class Auth(Resource):
    def post(self):
        body = request.get_json()
        order_review = OrderReviewDto(**body)
        OrderReviewDao.save(order_review)
        ....

class Access(Resource):
    def post(self):
        args = parser.parse_args()
        order_review = OrderReviewVo()
        ...