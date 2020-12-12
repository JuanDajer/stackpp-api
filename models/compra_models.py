from pydantic import BaseModel
from datetime import datetime

class CompraIn(BaseModel):
    alias: str
    producto: str
    cantidad: int

class CompraOut(BaseModel):
    id_compra: int
    alias: str
    date: datetime
    valor: float
    actual_saldo: float