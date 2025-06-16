from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    email = Column(String(150))
    password = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime)
