from pydantic import BaseModel

class ProductIn(BaseModel):
    nombre:str
    marca:str
    referencia:str
    costo:float
    cantidad:int
    descripcion:str
class ProductOut(BaseModel):
    id_producto: int
    nombre: str
    costo: float
    cantidad: int