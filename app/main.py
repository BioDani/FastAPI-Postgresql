from fastapi import FastAPI
from fastapi.params import Body

from .schemas.post import Post

app = FastAPI()
app.title = "Blog FastAPI - PostgreSQL"

@app.get("/")
async def root():
    return {"message": "Hello World, Daniel."}

@app.get("/posts")
async def root():
    return {"message": "Hello World, Daniel."}

@app.post("/createposts")
async def create_post(new_post: Post):
    print(new_post)
    return {"new_post": "data"}