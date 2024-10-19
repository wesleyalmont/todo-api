from datetime import datetime
from fastapi import HTTPException
from models.user import User


class UserService:
  

  @classmethod
  def get_user_by_id(cls, user_id: int) -> User:
    user = cls.get_user_by_id(user_id)
    if user:
      return user
    else:
      raise HTTPException(status_code=404, detail="User not found")


  def update_user(self, user: User) -> User:
    if user:
      user[user.id] = user
      return user
    else:
      raise HTTPException(status_code=400, detail="Cannot update user")

  @classmethod
  def delete_user(cls, user_id: int) :
    users = cls.get_user_by_id(user_id)
    if user_id in users:
      del users[user_id]
    else:
      raise HTTPException(status_code=404, detail="User not found")

  @classmethod
  def create_user(self, user: User) -> User:
    user = UserService.get_user_by_id(user.id)
    if user:
      return User(email="teste", name="teste", password="teste").model_dump()
    else:
      raise HTTPException(status_code=400, detail="This user already exists.")