from pydantic import BaseModel

class Mwave(BaseModel):
    name: str
    description: str
    completed: bool
    date: str
