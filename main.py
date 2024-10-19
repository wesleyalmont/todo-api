from fastapi import FastAPI

from routes.auth_route import auth_routes
from routes.todo_route import todo_routes
from routes.user_route import user_routes

app = FastAPI(version="0.0.1")
app.debug = True

app.include_router(auth_routes)
app.include_router(todo_routes)
app.include_router(user_routes)

app.get("/")
async def root():
  return {
    "versão": "0.0.1"
    }

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)