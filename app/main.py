from fastapi import FastAPI
from app . routers import items

app = FastAPI ()
# Registrar el router
app . include_router ( items . router , prefix ="/api/v1", tags =[",→ Items "])
