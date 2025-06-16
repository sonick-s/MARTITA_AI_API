from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TramiteBase(BaseModel):
    id_unidad: Optional[int]
    nombre: str
    descripcion: Optional[str]
    contexto: Optional[str]
    requisitos: Optional[str]
    pasos: Optional[str]
    links_formularios: Optional[str]

class TramiteCreate(TramiteBase):
    pass

class TramiteOut(TramiteBase):
    id_tramite: int
    fecha_registro: Optional[datetime]

    class Config:
        orm_mode = True
