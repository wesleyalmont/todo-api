from pydantic import BaseModel, ConfigDict


class Todo(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id = int
  title = str
  description = str
  completed = bool
  created_at = str
  updated_at = str

  def model_dump(self):
      data = super().model_dump()
      data["created_at"] = data["created_at"].isoformat()
      data["updated_at"] = data["updated_at"].isoformat()
      return data