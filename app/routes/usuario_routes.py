from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.usuario_controller as controller
from schemas.usuario_schema import UsuarioCreate, UsuarioOut
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    return controller.get_usuarios(db)

@router.get("/{id_}", response_model=UsuarioOut)
def obtener(id_: int, db: Session = Depends(get_db)):
    obj = controller.get_usuario(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@router.post("/", response_model=UsuarioOut)
def crear(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return controller.create_usuario(db, usuario)

@router.put("/{id_}", response_model=UsuarioOut)
def actualizar(id_: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    actualizado = controller.update_usuario(db, id_, usuario)
    if not actualizado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return actualizado

@router.delete("/{id_}", response_model=UsuarioOut)
def eliminar(id_: int, db: Session = Depends(get_db)):
    eliminado = controller.delete_usuario(db, id_)
    if not eliminado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return eliminado
