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


database_products = Dict[str, Producto]

database_products = {
    "Celular iPhone 7 32GB Negro Mate": Producto(**{"id_producto":1,
                                                    "nombre":"Celular iPhone 7 32GB Negro Mate",
                                                    "marca":"Apple",
                                                    "referencia":"iPhone 7",
                                                    "costo":849900,
                                                    "cantidad":5,
                                                    "descripcion":"Garantia 6 meses"}),
    "Celular Samsung Galaxy M31 128GB-Azul": Producto(**{"id_producto":2,
                                                        "nombre":"Celular Samsung Galaxy M31 128GB-Azul",
                                                        "marca":"Samsung",
                                                        "referencia":"Galaxy M31",
                                                        "costo":1149900,
                                                        "cantidad":10,
                                                        "descripcion":"Garantia 6 meses"}),
    "Celular Xiaomi Redmi Note 9S 64GB4GB DS Azul": Producto(**{"id_producto":3,
                                                                "nombre":"Celular Xiaomi Redmi Note 9S 64GB4GB DS Azul",
                                                                "marca":"Xiaomi",
                                                                "referencia":"Redmi Note 9S",
                                                                "costo":699900,
                                                                "cantidad":3,
                                                                "descripcion":"Garantia 6 meses"}),
    "Celular Motorola One Fusion Plus 128GB": Producto(**{"id_producto":4,
                                                            "nombre":"Celular Motorola One Fusion Plus 128GB",
                                                            "marca":"Motorola",
                                                            "referencia":"One Fusion Plus",
                                                            "costo":782900,
                                                            "cantidad":5,
                                                            "descripcion":"Garantia 6 meses"})
}
#Funciones sobre la base de datos ficticia
def get_producto(nombre: str):
    if nombre in database_products.keys():
        return database_products[nombre]
    else:
        return None

def update_producto(product: Producto):
    database_products[product.nombre] = product
    return product

def catalog_producto():
    lista =[]
    for i in database_products:
        a = "id producto:",database_products[i].id_producto,"Nombre:",database_products[i].nombre,"Costo:",database_products[i].costo,"Cantidades disponibles:",database_products[i].cantidad
        lista.append(a)
    return lista

generator = {"id_producto":4}
def save_product(product_created:Producto):
    if product_created.nombre in database_products.keys():
        return "Producto existente"
    else:
        generator["id_producto"] = generator["id_producto"] + 1
        product_created.id_producto=generator["id_producto"]
        a = {generator["id_producto"]:product_created}
        database_products.update(a)
        return product_created



