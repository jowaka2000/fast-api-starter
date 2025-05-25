from .. db.database import Base
from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime


class User(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)