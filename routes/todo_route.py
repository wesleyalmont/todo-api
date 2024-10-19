
from fastapi import APIRouter

from services.todo_service import TodoService

todo_routes = APIRouter()
todo_service = TodoService()

@todo_routes.get("/todos")
async def get_todos():
  pass


@todo_routes.post("/todos")
async def create_todos():
  pass


@todo_routes.put("/todos")
async def update_todos():
  pass


@todo_routes.delete("/todos")
async def delete_todos():
  pass