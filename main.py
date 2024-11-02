from fastapi import FastAPI, Response
import random

top = ["Armenians are the best", "AK is the best", "AK Tech Team - Top"]
app = FastAPI()


@app.get("/")
async def root():
    return Response(content="Hello, AK !!! Welcome to a new server :)")


@app.get("/some-facts")
async def say():
    return Response(content=random.choice(top), media_type="text/plain")
