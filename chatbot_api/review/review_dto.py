from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, DECIMAL, LONGTEXT
from sqlalchemy.orm import sessionmaker
from chatbot_api.ext.db import Base
from chatbot_api.user.user_dto import User
from chatbot_api.shop.shop_dto import Shop
from chatbot_api.food.food_dto import Food
from chatbot_api.review.review_dto import Review


class Review(Base) :
    __tablename__='review'

    review_id = Column(Integer, primary_key=True, index=True)
    review_cmnt = Column(VARCHAR(100))
    taste_rate = Column(Integer)
    quantity_rate = Column(Integer)
    delivery_rate = Column(Integer)
    review_time = Column(Integer)
    review_img = Column(LONGTEXT)
    userid = Column(VARCHAR(20), ForeignKey('User.userid'))
    shop_id = Column(Integer, ForeignKey('Shop.shop_id'))
    food_id = Column(Integer, ForeignKey('Food.food_id'))

    def __repr__(self):
        pass

    @property
    def serialise(self):
        return {
            'order_id' : self.order_id
            'order_time' : self.order_time
            'order_cmnt' : self.order_cmnt
            'userid' : self.userid
            'shop_id' : self.shop_id
            'food_id' : self.food_id
            'review_id' : self.review_id
        }

class OrderDto(object) :
    order_id : int 
    order_time : int
    order_cmnt : str
    userid : str
    shop_id : int
    food_id : int
    review_id : int
    
