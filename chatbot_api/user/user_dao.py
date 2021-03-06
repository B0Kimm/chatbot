from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from chatbot_api.ext.db import Base
from chatbot_api.user import User
'''
어플리케이션이 SQLAlchemy ORM을 사용한다면, 
객체에 바인딩된 쿼리를 위해서 Session 객체를 사용해야 한다. 
이는 session.add(), session.rollback(), session.commit(), session.close()를 통해 
트랜잭션을 단일 작업 단위로 관리하기 좋고, 
이러한 특징을 통해 Python의 Context Manager 패턴을 사용하기에도 좋다.
'''
class UserDao():
    def __init__(self):
         self.engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
       
    def create_table(self):
        Base.metadata.create_all(self.engine)

    def insert_user(self):
        session.add(User(userid='tom', password='1', name='thomas'))
        session.commit()

    def fetch_user(self):
        query = session.query(User).filter((User.userid == 'tom'))
        return query[0]