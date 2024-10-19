from fastapi import APIRouter
from helpers.api_response import APIResponse
from models.user import User
from services.users_service import UserService
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

user_routes = APIRouter()
user_service = UserService()

@user_routes.get("/users", response_model=APIResponse)
async def get_users():
    return APIResponse.handle_response(fn=user_service.get_users)

@user_routes.get("/users/{user_id}", response_model=APIResponse)
async def get_user_by_id(user_id: int):
    return APIResponse.handle_response(fn=lambda: user_service.get_user_by_id(user_id))

@user_routes.post("/users", response_model=APIResponse)
async def create_user(user: User):
    return APIResponse.handle_response(fn=lambda: user_service.create_user(user))

@user_routes.put("/users/{user_id}", response_model=APIResponse)
async def update_user(user_id: int, user: User):
    return APIResponse.handle_response(fn=lambda: user_service.update_user(user_id, user))

@user_routes.delete("/users/{user_id}", response_model=APIResponse)
async def delete_user(user_id: int):
    return APIResponse.handle_response(fn=lambda: user_service.delete_user(user_id))
