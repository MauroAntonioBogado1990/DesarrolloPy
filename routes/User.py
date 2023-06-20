from fastapi import APIRouter,HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int 
    name: str
    lastname: str 
    email: str

usuarios = [User(id=0,name="Mauro", lastname="Bogado",email="maurobogado@correo.com")]

router = APIRouter()

#vamos a listar usuarios
@router.get("/users")
async def get_users():
    return usuarios

#retorno de usuario
@router.get("/user/{id}")
async def user(id: int):
    if id not in usuarios:
        return buscar_usuarios(id)
    else:
        return "Usuario no encontrado"
    
#para agregar un usuario
@router.post("/users/", status_code=201)
async def create_user(user: User):
    # if(type.Item)
    usuarios.append(user)

#creamos una funcion para modular la busqueda
def buscar_usuarios(id:int):
    s = filter(lambda usuario: usuario.id == id, usuarios)
    try:
        return list(s)[0]
    except:
        raise HTTPException(status_code=204,detail="No se encontró el usuario")
