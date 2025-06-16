from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.prompt_bot_controller as controller
from schemas.prompt_bot_schema import PromptBotCreate, PromptBotOut
from typing import List

router = APIRouter(prefix="/prompts", tags=["Prompts Bot"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PromptBotOut])
def listar(db: Session = Depends(get_db)):
    return controller.get_prompts(db)

@router.get("/{id_}", response_model=PromptBotOut)
def obtener(id_: int, db: Session = Depends(get_db)):
    obj = controller.get_prompt(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@router.post("/", response_model=PromptBotOut)
def crear(prompt: PromptBotCreate, db: Session = Depends(get_db)):
    return controller.create_prompt(db, prompt)

@router.put("/{id_}", response_model=PromptBotOut)
def actualizar(id_: int, prompt: PromptBotCreate, db: Session = Depends(get_db)):
    actualizado = controller.update_prompt(db, id_, prompt)
    if not actualizado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return actualizado

@router.delete("/{id_}", response_model=PromptBotOut)
def eliminar(id_: int, db: Session = Depends(get_db)):
    eliminado = controller.delete_prompt(db, id_)
    if not eliminado:
        raise HTTPException(status_code=404, detail="No encontrado")
    return eliminado
