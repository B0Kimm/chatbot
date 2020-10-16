from sqlalchemy import Column, Integer 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT
from chatbot_api.ext.db import Base

class User(Base):

    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    userid = Column(VARCHAR(20), primary_key = True, index = True)
    pwd = Column(VARCHAR(200))
    name = Column(VARCHAR(30))
    addr = Column(VARCHAR(100))
    lat = Column(VARCHAR(40))
    lng = Column(VARCHAR(40))

    def __repr__(self):
        return f'User(id={self.id},userid={self.userid},\
            password={self.password},name={self.name})'

    @property
    def serialize(self):
        return {
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name,
            'addr' : self.addr
            'lat' : self.lat
            'lng' : self.lng
        }



class UserDto(object):
    userid: str
    password: str
    name: str
    addr : str
    lat : str
    lng : str
