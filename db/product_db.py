from typing import Dict
from pydantic import BaseModel

#Definición de Producto
class Producto(BaseModel):
    id_producto: int
    nombre: str
    marca: str
    referencia: str
    costo: float
    cantidad: int
    descripcion: str

# Base de datos ficticia 
database_products = Dict[int, Producto]
database_products = {
    1: Producto(**{"id_producto":1,
                    "nombre":"Celular iPhone 7 32GB Negro Mate",
                    "marca":"Apple",
                    "referencia":"iPhone 7",
                    "costo":849900,
                    "cantidad":5,
                    "descripcion":"Garantia 6 meses"}),
    2: Producto(**{"id_producto":2,
                    "nombre":"Celular Samsung Galaxy M31 128GB-Azul",
                    "marca":"Samsung",
                    "referencia":"Galaxy M31",
                    "costo":1149900,
                    "cantidad":10,
                    "descripcion":"Garantia 6 meses"}),
    3: Producto(**{"id_producto":3,
                    "nombre":"Celular Xiaomi Redmi Note 9S 64GB4GB DS Azul",
                    "marca":"Xiaomi",
                    "referencia":"Redmi Note 9S",
                    "costo":699900,
                    "cantidad":3,
                    "descripcion":"Garantia 6 meses"}),
    4: Producto(**{"id_producto":4,
                    "nombre":"Celular Motorola One Fusion Plus 128GB",
                    "marca":"Motorola",
                    "referencia":"One Fusion Plus",
                    "costo":782900,
                    "cantidad":5,
                    "descripcion":"Garantia 6 meses"}),
}
#Funciones sobre la base de datos ficticia
def get_producto(id_producto: int):
    if id_producto in database_products.keys():
        return database_products[id_producto]
    else:
        return None

def update_producto(product: Producto):
    database_products[product.id_producto] = product
    return product