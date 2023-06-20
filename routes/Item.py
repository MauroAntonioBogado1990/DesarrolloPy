from fastapi import APIRouter,HTTPException
from pydantic import BaseModel


#desarrollamos los modelos
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: str 
    quantity: int
    company : str


productos = [Item(id=0,name="pantalon",description="Tela de jean",company="Levis",price=2100.0,tax="38",quantity=3)]

router = APIRouter()

#Agregado de la ruta de productos
@router.get("/items/{id}")
async def read_item(id:int):
    if id not in productos:
        return buscar_productos(id)    
    return HTTPException(status_code=204, detail="Producto no encontrado")#"Producto no encontrado"

#Creacion de productos
@router.post("/items/", status_code=201)
async def create_item(producto: Item):
    if type(buscar_productos(producto.id))==Item:
        return {'error' : 'El producto ya existe'}
       
    else:
        return productos.append(producto)

#agregado de un nuevo item
@router.get("/items")
async def get_items():
    return productos   
 
#actualizar un producto
@router.put("/items/",status_code=201)
async def update_product(producto:Item):

    for index, productoAGuardar in enumerate(productos):
        if productoAGuardar.id == producto.id:
            productos[index] = producto  
        else:
            return {'error':'No su puede actualizar el producto'} 
            
#a eliminar el producto
@router.delete("/items/{id}", status_code=401)
async def eliminate_product(id:int):
    for index, productoAEliminar in enumerate(productos):
        if productoAEliminar.id == id:
            del productos[index]
       

    
def buscar_productos(id:int):
    s = filter(lambda producto: producto.id == id, productos)
    try:
        return list(s)[0]
    except:
        raise HTTPException(status_code=204,detail="No se encontró el producto")