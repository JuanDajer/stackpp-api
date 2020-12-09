from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.product_db import Producto
from db.product_db import get_producto, update_producto, catalog_producto
from db.compra_db import CompraInDB
from db.compra_db import save_compra

from models.user_models import UserIn, UserOut
from models.compra_models import CompraIn, CompraOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/user/saldo/{alias}")
async def get_saldo(alias: str):
    user_in_db = get_user(alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/compra/")
async def make_compra(compra_in: CompraIn):
    user_in_db = get_user(compra_in.alias)
    producto_in_db = get_producto(compra_in.producto)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if producto_in_db.cantidad<compra_in.cantidad:
        raise HTTPException(status_code=400,
                            detail="Sin inventario suficiente")
    if user_in_db.saldo < compra_in.cantidad * producto_in_db.costo:
        raise HTTPException(status_code=400,
                            detail="Sin fondos suficientes")

    user_in_db.saldo = user_in_db.saldo - (compra_in.cantidad * producto_in_db.costo)
    update_user(user_in_db)
    compra_in_db = CompraInDB(**compra_in.dict(),
                                actual_saldo = user_in_db.saldo,valor =compra_in.cantidad * producto_in_db.costo)
    compra_in_db = save_compra(compra_in_db)
    compra_out = CompraOut(**compra_in_db.dict())
    return compra_out

@api.post("/product/catalogo/")
async def catalog_product():
    return catalog_producto()

