from db.user_db import usuario_data, usuario_data
from db.user_db import get_user, create_user

from models.user_models import User

from fastapi import FastAPI, HTTPException
from typing import Optional

api = FastAPI()

#https://sprint-2-12.herokuapp.com/user/create/
@api.post("/user/create/")
async def crear_usuario(usuario: usuario_data):
    
    usr = get_user(usuario.userdocument)    
        
    if (usr != None):
        raise HTTPException(status_code=404, detail="Usuario ya existe")
    #elif (usuario.id <= usr.id):
    #    raise HTTPException(status_code=404, detail=f"El id del user ya esta en uso, puede elegir el número ${usuario.id + 1}")
    elif (usuario.userdocument == False):
        raise HTTPException(status_code=404, detail="Escriba un nombre válido")
    else:
        create_user(usuario)
    return  usuario

#https://sprint-2-12.herokuapp.com/user/{username}
@api.get("/user/{userdocument}")
async def listar_usuario(document_user: int):
    
    usuario = get_user(document_user)
    
    if usuario == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    info_usuario = usuario.dict()
    
    return info_usuario