# Put the code for your API here.

# Imports
from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


test commit