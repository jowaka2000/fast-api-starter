from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data':"this is index page"}