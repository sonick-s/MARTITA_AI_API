from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.interaccion_controller as controller
from schemas.interaccion_schema import InteraccionCreate, InteraccionOut
from typing import List

router = APIRouter(prefix="/interacciones", tags=["Interacciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[InteraccionOut])
def listar(db: Session = Depends(get_db)):
    return controller.get_interacciones(db)

@router.get("/{id_}", response_model=InteraccionOut)
def obtener(id_: int, db: Session = Depends(get_db)):
    obj = controller.get_interaccion(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@router.post("/", response_model=InteraccionOut)
def crear(interaccion: InteraccionCreate, db: Session = Depends(get_db)):
    return controller.create_interaccion(db, interaccion)

@router.put("/{id_}", response_model=InteraccionOut)
def actualizar(id_: int, interaccion: InteraccionCreate, db: Session = Depends(get_db)):
    actualizado = controller.update_interaccion(db, id_, interaccion)
    if not actualizado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return actualizado

@router.delete("/{id_}", response_model=InteraccionOut)
def eliminar(id_: int, db: Session = Depends(get_db)):
    eliminado = controller.delete_interaccion(db, id_)
    if not eliminado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return eliminado
