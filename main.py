from fastapi import FastAPI
from pydantic import BaseModel
from DesarrolloPy.models import Item

class User(BaseModel):
    id: int 
    name: str
    lastname: str 
    email: str

productos = [Item(id=0,name="pantalon",description="Tela de jean",company="Levis",price=2100.0,tax="38",quantity=3)]
usuarios = [User(id=0,name="Mauro", lastname="Bogado",email="maurobogado@correo.com")]
app = FastAPI()


#pagina principal
@app.get("/")
async def root():
    return "Página de Bienvenida"

#vamos a listar usuarios
@app.get("/users")
async def get_users():
    return usuarios

#retorno de usuario
@app.get("/user/{id}")
async def user(id: int):
    if id not in usuarios:
        return buscar_usuarios(id)
    else:
        return "Usuario no encontrado"
    
#para agregar un usuario
@app.post("/users/")
async def create_user(user: User):
    # if(type.Item)
    usuarios.append(user)

#Agregado de la ruta de productos
@app.get("/items/{id}")
async def read_item(id:int):
    if id not in productos:
        return buscar_productos(id)    
    return "Producto no encontrado"

#Creacion de productos
@app.post("/items/")
async def create_item(producto: Item):
    if type(buscar_productos(producto.id))==Item:
        return {'error' : 'El producto ya existe'}
       
    else:
        return productos.append(producto)

#agregado de un nuevo item
@app.get("/items")
async def get_items():
    return productos   
 
#actualizar un producto
@app.put("/items")
async def update_product(producto:Item):
    for index, producto in enumerate in (productos):
        if productos[]
#usamos un metodo para la busqueda de productos
# @app.post("/items/{item_id:int:int")
# def search_product(Item_id):
#     return lambda 

#creamos una funcion para modular la busqueda
def buscar_usuarios(id:int):
    s = filter(lambda usuario: usuario.id == id, usuarios)
    try:
        return list(s)[0]
    except:
        return {"error": "No se ha encontrado"}
    
def buscar_productos(id:int):
    s = filter(lambda producto: producto.id == id, productos)
    try:
        return list(s)[0]
    except:
        return {"error": "No se ha encontrado"}