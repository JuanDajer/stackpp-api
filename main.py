from db.user_db import UserInDB
from db.user_db import update_user, get_user, save_user, lista_user, delete_usuario
'''from db.product_db import Producto
from db.product_db import get_producto, update_producto, catalog_producto, save_product
from db.compra_db import CompraInDB
from db.compra_db import save_compra'''

from models.user_models import UserIn, UserOut, UserCash, UserGet
'''from models.compra_models import CompraIn, CompraOut
from models.product_moldels import ProductIn , ProductOut'''

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/user/saldo/")
async def get_saldo(user_get: UserGet):
    user_in_db = get_user(user_get.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.post("/user/create/")
async def create_user(userIn: UserInDB):
    user_in_db = UserInDB(**userIn.dict())
    return save_user(user_in_db)

@api.get("/user/lista/")
async def user_list():
    return lista_user()

@api.put("/user/credito/")
async def user_credito(user_cred: UserCash):
    user_in_db = get_user(user_cred.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    else:
        user_in_db.saldo = user_in_db.saldo + user_cred.valor
        update_user(user_in_db)
        return "Usuario:",user_in_db.alias,"Nuevo saldo:",user_in_db.saldo

@api.delete("/user/borrar/")
async def user_delete(user_get: UserGet):
    usuario = get_user(user_get.alias)
    if usuario == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    else:  
        delete_usuario(usuario.alias)
        raise HTTPException(status_code=200,
                                detail="El usuario ha sido eliminado")

'''@api.put("/user/compra/")
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
    producto_in_db.cantidad = producto_in_db.cantidad - compra_in.cantidad
    update_producto(producto_in_db)
    compra_in_db = CompraInDB(**compra_in.dict(),
                                actual_saldo = user_in_db.saldo,valor =compra_in.cantidad * producto_in_db.costo)
    compra_in_db = save_compra(compra_in_db)
    compra_out = CompraOut(**compra_in_db.dict())
    return compra_out

@api.post("/product/catalogo/")
async def catalog_product():
    return catalog_producto()

@api.put("/product/create/")
async def create_product(productoIn: ProductIn):
    producto_in_db = Producto(**productoIn.dict(),id_producto=0)
    return save_product(producto_in_db)
'''










