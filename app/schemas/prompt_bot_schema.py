from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PromptBotBase(BaseModel):
    nombre: str
    tipo: Optional[str]
    contenido: str
    prioridad: Optional[int] = 0

class PromptBotCreate(PromptBotBase):
    pass

class PromptBotOut(PromptBotBase):
    id_prompt: int
    fecha_creacion: Optional[datetime]

    class Config:
        orm_mode = True
