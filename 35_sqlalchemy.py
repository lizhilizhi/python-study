from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column ,Integer,String


engine = create_engine("mysql+pymysql://username:@localhost:3306/renren_fast",echo = True)

Base = declarative_base()

class User(Base):
    __tablename__='user' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)



