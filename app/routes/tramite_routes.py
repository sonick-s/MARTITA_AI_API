from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.tramite_controller as controller
from schemas.tramite_schema import TramiteCreate, TramiteOut
from typing import List

router = APIRouter(prefix="/tramites", tags=["Trámites"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TramiteOut])
def listar(db: Session = Depends(get_db)):
    return controller.get_tramites(db)

@router.get("/{id_}", response_model=TramiteOut)
def obtener(id_: int, db: Session = Depends(get_db)):
    obj = controller.get_tramite(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@router.post("/", response_model=TramiteOut)
def crear(tramite: TramiteCreate, db: Session = Depends(get_db)):
    return controller.create_tramite(db, tramite)

@router.put("/{id_}", response_model=TramiteOut)
def actualizar(id_: int, tramite: TramiteCreate, db: Session = Depends(get_db)):
    actualizado = controller.update_tramite(db, id_, tramite)
    if not actualizado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return actualizado

@router.delete("/{id_}", response_model=TramiteOut)
def eliminar(id_: int, db: Session = Depends(get_db)):
    eliminado = controller.delete_tramite(db, id_)
    if not eliminado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return eliminado
