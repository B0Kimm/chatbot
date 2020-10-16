from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, DECIMAL, LONGTEXT
from sqlalchemy.orm import sessionmaker
from chatbot_api.ext.db import Base
from chatbot_api.shop.shop_dto import Shop



class Food(Base) :
    __tablename__='food'

    food_id = Column(Integer, primary_key=True, index=True)
    food_name = Column(VARCHAR(50))
    price = Column(Integer)
    food_rev_avg = Column(Integer)
    food_rev_amt = Column(Integer)
    shop_id = Column(Integer, ForeignKey('Shop.shop_id'))


    def __repr__(self):
        return f'Food(food_id = {food_id},\
        food_name = {food_name},\
        price = {price},\
        food_rev_avg = {food_rev_avg},\
        food_rev_amt = {food_rev_amt},\
        shop_id = {fshop_id})'


    @property
    def serialise(self):
        return {
            food_id : self.food_id
            food_name : self.food_name
            price : self.price
            food_rev_avg : self.food_rev_avg
            food_rev_amt : self.food_rev_amt
            shop_id : self.shop_id
        }

class OrderDto(object) :
    food_id : int
    food_name : str
    price : int
    food_rev_avg : int  
    food_rev_amt : int
    shop_id : int
    
