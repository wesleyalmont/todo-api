
from models.user import User


class AuthService:

  @classmethod
  def login(self, user: User):
    user.email = user.email.lower()
    return user
  

  @classmethod
  def register(self):
    pass

  def logout(self):
    pass

  def generate_token(self):
    pass