from pydantic import BaseModel
from typing import Optional
from datetime import date

class DireccionBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    responsable: Optional[str] = None
    correo_responsable: Optional[str] = None
    telefono: Optional[str] = None
    fecha_actualizacion: Optional[date] = None

class DireccionCreate(DireccionBase):
    pass

class DireccionOut(DireccionBase):
    id_direcciones: int

    class Config:
        orm_mode = True
