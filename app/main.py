from fastapi import FastAPI
from .models import models
from .db.database import Base,engine
from . routers import authentication

app = FastAPI()


# migrate all in the db
models.Base.metadata.create_all(engine)

# auth router
app.include_router(authentication.router)




# test router
@app.get('/',tags=['Test'])
def index():
    return {'data':"this is index page"}