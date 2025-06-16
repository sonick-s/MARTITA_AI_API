from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: Optional[str]
    email: Optional[EmailStr]
    password: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: Optional[str]
    email: Optional[EmailStr]
    fecha_registro: Optional[datetime]

    class Config:
        orm_mode = True
