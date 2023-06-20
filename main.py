from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from routes import Item,User

# class User(BaseModel):
#     id: int 
#     name: str
#     lastname: str 
#     email: str

#productos = [Item(id=0,name="pantalon",description="Tela de jean",company="Levis",price=2100.0,tax="38",quantity=3)]
#usuarios = [User(id=0,name="Mauro", lastname="Bogado",email="maurobogado@correo.com")]
app = FastAPI()

#importamos los routers
app.include_router(Item.router)
app.include_router(User.router) 

#pagina principal
@app.get("/")
async def root():
    return "Página de Bienvenida"

# #vamos a listar usuarios
# @app.get("/users")
# async def get_users():
#     return usuarios

# #retorno de usuario
# @app.get("/user/{id}")
# async def user(id: int):
#     if id not in usuarios:
#         return buscar_usuarios(id)
#     else:
#         return "Usuario no encontrado"
    
# #para agregar un usuario
# @app.post("/users/", status_code=201)
# async def create_user(user: User):
#     # if(type.Item)
#     usuarios.append(user)

# #Agregado de la ruta de productos
# @app.get("/items/{id}")
# async def read_item(id:int):
#     if id not in productos:
#         return buscar_productos(id)    
#     return HTTPException(status_code=204, detail="Producto no encontrado")#"Producto no encontrado"

# #Creacion de productos
# @app.post("/items/", status_code=201)
# async def create_item(producto: Item):
#     if type(buscar_productos(producto.id))==Item:
#         return {'error' : 'El producto ya existe'}
       
#     else:
#         return productos.append(producto)

# #agregado de un nuevo item
# @app.get("/items")
# async def get_items():
#     return productos   
 
# #actualizar un producto
# @app.put("/items/",status_code=201)
# async def update_product(producto:Item):

#     for index, productoAGuardar in enumerate(productos):
#         if productoAGuardar.id == producto.id:
#             productos[index] = producto  
#         else:
#             return {'error':'No su puede actualizar el producto'} 
            
# #a eliminar el producto
# @app.delete("/items/{id}", status_code=401)
# async def eliminate_product(id:int):
#     for index, productoAEliminar in enumerate(productos):
#         if productoAEliminar.id == id:
#             del productos[index]
       
               
        

# #usamos un metodo para la busqueda de productos
# # @app.post("/items/{item_id:int:int")
# # def search_product(Item_id):
# #     return lambda 

# #creamos una funcion para modular la busqueda
# def buscar_usuarios(id:int):
#     s = filter(lambda usuario: usuario.id == id, usuarios)
#     try:
#         return list(s)[0]
#     except:
#         raise HTTPException(status_code=204,detail="No se encontró el usuario")
    
# def buscar_productos(id:int):
#     s = filter(lambda producto: producto.id == id, productos)
#     try:
#         return list(s)[0]
#     except:
#         raise HTTPException(status_code=204,detail="No se encontró el producto")