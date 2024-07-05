from fastapi import APIRouter
from ..schemas.post import Post

router_post = APIRouter(prefix="/post")

@router_post.post("/add")
async def add_post(new_post: Post):
    print(new_post)
    return {"new_post": new_post}