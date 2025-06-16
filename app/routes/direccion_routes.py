from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.direccion_controller as controller
from schemas.direccion_schema import DireccionCreate, DireccionOut
from typing import List

router = APIRouter(prefix="/direcciones", tags=["Direcciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[DireccionOut])
def listar(db: Session = Depends(get_db)):
    return controller.get_direcciones(db)

@router.get("/{id_}", response_model=DireccionOut)
def obtener(id_: int, db: Session = Depends(get_db)):
    obj = controller.get_direccion(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@router.post("/", response_model=DireccionOut)
def crear(direccion: DireccionCreate, db: Session = Depends(get_db)):
    return controller.create_direccion(db, direccion)

@router.put("/{id_}", response_model=DireccionOut)
def actualizar(id_: int, direccion: DireccionCreate, db: Session = Depends(get_db)):
    actualizada = controller.update_direccion(db, id_, direccion)
    if not actualizada:
        raise HTTPException(status_code=404, detail="No encontrado")
    return actualizada

@router.delete("/{id_}", response_model=DireccionOut)
def eliminar(id_: int, db: Session = Depends(get_db)):
    eliminada = controller.delete_direccion(db, id_)
    if not eliminada:
        raise HTTPException(status_code=404, detail="No encontrado")
    return eliminada
