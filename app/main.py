# Imports from fastapi
from fastapi import FastAPI
from fastapi.params import Body

# Schemas
from .schemas.post import Post

# Routers
from .routers.healh_check import router_health_check
from .routers.posts import router_post

# Run app and server
app = FastAPI()
app.title = "Blog FastAPI - PostgreSQL"
app.description = "Simple rest-full API with PostgreSQL."
app.version = "1.0"

app.include_router(router_health_check)
app.include_router(router_post)