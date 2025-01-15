import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_env():
    return {'env': os.environ['ENVIRONMENT']}