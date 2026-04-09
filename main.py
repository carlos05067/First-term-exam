from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel
from typing import Optional
app = FastAPI()

class User(SQLModel):
    id: int
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

#contador para usuarios ----------------------------------------------------
contador_id = 0
def generar_id():
    global contador_id
    contador_id += 1
    return contador_id
#---------------------------------------------------------------------------
db_users={}

@app.get("/")
def bienvenida():
    return {"mensaje": "Bienvenido a mi fastapi"}

#cracion de usuariio -------------------------------------------------------
@app.post("/usuarios/")
def crear_usuario(usuario:User):
    for usuario_existente in db_users.values():
        if usuario_existente.username == usuario.username:
            return{"mensaje":"Ese usuario ya existe"}
    nuevo_id = generar_id()
    usuario.id = nuevo_id
    db_users[nuevo_id]=usuario
    return{"mensaje":"Usuario creado"}

#listar usuarios -----------------------------------------------------------
@app.get("/usuarios/")
def listar_usuarios():
    return list(db_users.values())

#obtener usuario -----------------------------------------------------------
@app.get("/usuarios/{id}")
def obtener_usuarios(id:int):
    if id not in db_users:
        return{"mensaje":"Usuario no encontrado"}
    usuario = db_users[id]
    return usuario

#actualizacion de usuario --------------------------------------------------
@app.put("/usuarios/{id}")
def actualizar_usuario(id:int, usuario_actuializado:User):
    if id in db_users:
        db_users[id].username = usuario_actuializado.username
        db_users[id].email = usuario_actuializado.email
        return{"mensaje":f"Usuario actualizado con id: {id}"}
    return{"mensaje":"Usuario no encontrado"}

#eliminacion de usuario ----------------------------------------------------
@app.delete("/usuarios/{id}")
def eliminar_usuario(id:int):
    if id in db_users:
        db_users[id].is_active = False
        return{"mensaje":f"Usuario eliminado con id:{id}"}
    return{"mensaje":"Usuario no encontrado"}
#login de usuario ----------------------------------------------------------
@app.post("/login")
def login(user: User):
    for db_user in db_users.values():
        if db_user.username == user.username and db_user.password == user.password:
            return {"status": "success", "message": f"Bienvenido, {user.username}!"}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")