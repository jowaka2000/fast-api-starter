from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(tags=['Authentication'],prefix='/login')



@router.post('/')
def login(req:OAuth2PasswordRequestForm=Depends()):
    
    # get user and verify password
    
    
    # get token 
    #   access_token = token.create_access_token(data={"sub":user.email})
    pass