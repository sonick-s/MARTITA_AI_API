from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InteraccionBase(BaseModel):
    pregunta: str
    respuesta: str
    respuesta_util: Optional[str] = None

class InteraccionCreate(InteraccionBase):
    pass

class InteraccionOut(InteraccionBase):
    id_interaccion: int
    fecha: Optional[datetime]

    class Config:
        orm_mode = True
