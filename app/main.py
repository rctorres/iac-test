import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_env():
    # Get all environment variables and format them as JSON
    env_vars = {}
    for key, value in os.environ.items():
        env_vars[key] = value
    return env_vars