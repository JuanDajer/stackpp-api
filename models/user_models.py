from pydantic import BaseModel

class UserIn(BaseModel):
    alias: str
    password: str
class UserOut(BaseModel):
    alias: str
    saldo: float
class UserCash(BaseModel):
    alias: str
    valor: float

