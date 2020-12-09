from datetime import datetime
from pydantic import BaseModel

#Definicion de compra
class CompraInDB(BaseModel):
    id_compra: int = 0
    alias: str
    date: datetime = datetime.now()
    valor: float
    actual_saldo: float

database_compra = []
generator = {"id":0}

def save_compra(compra_in_db: CompraInDB):
    generator["id"] = generator["id"] + 1
    compra_in_db.id_compra = generator["id"]
    database_compra.append(compra_in_db)
    return compra_in_db

