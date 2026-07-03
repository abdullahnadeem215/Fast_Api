from pydantic import BaseModel

class user_Response(BaseModel):
    id : int
    name: str
    qty:int=0

class item(BaseModel):
    id : int
    name: str
    qty:int=0
    password:str