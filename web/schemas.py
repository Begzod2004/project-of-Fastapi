from pydantic import BaseModel

class Cotigory(BaseModel):
    name: str
    description: str

class SubCotigory(BaseModel):
    name: str
    description: str
    cotigory: Cotigory