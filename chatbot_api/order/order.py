from chatbot_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship , backref
from sqlalchemy.dialects.mysql import VARCHAR, DECIMAL, LONGTEXT

class Order(Base) :
    __tablename__='order'

    order_id = Column(Integer, primary_key=True, index=True)
    order_time = Column(Integer)
    order_cmnt = Column(LONGTEXT)
    userid = Column(VARCHAR(20), ForeignKey('user.userid'))
    # user = relationship('User', backref=backref('addresses', order_by=userid))
    shop_id= Column(Integer)
    food_id = Column(Integer)
    review_id = Column(Integer)

engine = create_engine('mysql+mysqlconnector://root:1793456@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

session.commit()