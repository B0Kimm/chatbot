from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot_api.ext.db import Base
from chatbot_api.food.food_dto import Food

class FoodDao() :
    def __init__(self) :
        self.engine = create_engine('mysql+mysqlconnector://root:1793456@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def create_table(self) :
        Base.metadata.create_all(self.engine)

    def add_food(self, food):
        session.add(food)
        session.commit()

    # def fetch_order(self, order_id) :
    #     query = session.query(Order).filter((Order.order_id == f'{order_id}'))
    #     return query[0] # query[0]???????

    # def fetch_all_order(self):
    #     return session.query(Order).all()

    # def update_order(self):
    #     query = session.query(Order).filter((User.userid == userid))
    #     return pass

    # def delete_order(self):
    #     query = session.query(Order).filter((User.userid == userid))
    #     return pass


# dto는 json과 연동
# table 생성 => json으로 변동

