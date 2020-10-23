from chatbot_api.ext.db import db, openSession
from chatbot_api.order_review.service import OrderReviewService
from chatbot_api.order_review.dto import OrderReviewDto
import pandas as pd
import json

class OrderReviewDao(OrderReviewDto):
    @classmethod
    def find_all(cls) :
        return cls.query.all()
    
    @classmethod
    def find_by_time(cls, order_time) :
        return cls.query.filter_by(order_time == order_time).all()

    @classmethod
    def fetch_by_userid(cls, userid) :
        return cls.query.filter_by(userid == userid).first()

    @classmethod
    def fetch_by_shop_id(cls, shop_id):
        return cls.query.filter_by(shop_id == shop_id).first()

    @classmethod
    def fetch_by_food_id(cls, food_id):
        return cls.query.filter_by(food_id == food_id).first()

    @classmethod
    def fetch_by_review_id(cls, review_id):
        return cls.query.filter_by(review_id == review_id).first()