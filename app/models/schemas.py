from pydantic import BaseModel
from typing import Optional




class User(BaseModel):
    name:str
    email:str
    password:str
    

class ShowUser(BaseModel):
    name:str
    email:str
    
    class Config():
        orm_mode=True








#authentication
class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    email:Optional[str]=None