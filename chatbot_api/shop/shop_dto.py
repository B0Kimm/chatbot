from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, DECIMAL, LONGTEXT
from sqlalchemy.orm import sessionmaker
from chatbot_api.ext.db import Base


class Shop(Base) :
    __tablename__='shop'

    shop_id = Column(Integer, primary_key=True, index=True)
    shop_name = Column(VARCHAR(100))
    shop_addr = Column(VARCHAR(100))
    cat = Column(VARCHAR(100))
    shop_lat = Column(Integer)
    shop_lng = Column(Integer)
    shop_rev_avg = Column(Integer)
    shop_rev_amt = Column(Integer)
    opentime = Column(Integer)

    def __repr__(self):
        pass

    @property
    def serialise(self):
        return {
                shop_id :
                shop_name :
                shop_addr :
                cat :
                shop_lat :
                shop_lng :
                shop_rev_avg :
                shop_rev_amt :
                opentime :
        }

class ShopDto(object) :
    shop_id : str
    shop_name : str
    shop_addr : str
    cat : str
    shop_lat : int
    shop_lng : int
    shop_rev_avg : int
    shop_rev_amt : int
    opentime : int
    
