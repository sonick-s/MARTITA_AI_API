# app/main.py
from fastapi import FastAPI
from database import engine, Base # Assuming you have these
from routes import (
    direccion_routes, tramite_routes, usuario_routes,
    interaccion_routes, prompt_bot_routes
)
# ... import other models

# Create database tables (This is often done with Alembic in production)
# user_models.Base.metadata.create_all(bind=engine)
# (Call .create_all() on the Base that all your models inherit from)


app = FastAPI()

app.include_router(direccion_routes.router)
app.include_router(tramite_routes.router)
app.include_router(usuario_routes.router)
app.include_router(interaccion_routes.router)
app.include_router(prompt_bot_routes.router)

@app.get("/")
def read_root():
    # __  __   _   ___ _____ ___ _____ _         ___   _   
    # |  \/  | /_\ | _ \_   _|_ _|_   _/_\      |_ _| /_\  
    # | |\/| |/ _ \|   / | |  | |  | |/ _ \      | | / _ \ 
    # |_|  |_/_/ \_\_|_\ |_| |___| |_/_/ \_\____|___/_/ \_\
    #                                       |___|         

    return {"message": "Bienvenido a la API de Martita IA, creada como trabajo de grado -Jean De La Cruz , Omar Sani"}