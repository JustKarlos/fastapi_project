from fastapi import APIRouter , HTTPException
from app . models . item_model import Item
router = APIRouter ()

# Base de datos simulada
items_db = {}
@router . get ("/ items ", summary =" Obtener todos los tems ")
def get_items () :
  return {" items ": list ( items_db . values () ) } 
  
@router . get ("/ items /{ item_id }", summary =" Obtener un tem por,→ ID")
def get_item ( item_id : int) :
  if item_id not in items_db :
    raise HTTPException ( status_code =404 , detail =" Item no,→ encontrado ")
return items_db [ item_id ]

@router . post ("/ items ", summary =" Crear un nuevo tem ")
def create_item ( item_id : int , item : Item ) :
  if item_id in items_db :
    raise HTTPException ( status_code =400 , detail ="ID ya,→ existe ")
    items_db [ item_id ] = item . dict ()
return {" message ": " tem creado ", " item ": item }
