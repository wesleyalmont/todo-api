

from fastapi import APIRouter

from helpers.api_response import APIResponse
from models.user import User
from services.auth_service import AuthService


auth_routes = APIRouter()

@auth_routes.post("/login")
async def login(user: User):
  try:
    AuthService.login()
  except Exception as e:
    print(e)
  APIResponse.handle_response(fn=AuthService.login )

@auth_routes.post("/logout")
async def logout():
  pass
