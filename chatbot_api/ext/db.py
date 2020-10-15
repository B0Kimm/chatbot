from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

config = {
    'user' : 'root',
    'password' : '1793456',
    'host' : 'localhost',
    'port': '3306',
    'database' : 'mariadb'

}

# root에 정의하면 static 객체가 된다.