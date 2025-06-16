from sqlalchemy import Column, Integer, String, Text, Date
from database import Base

class Direccion(Base):
    __tablename__ = 'direcciones'
    
    id_direcciones = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    responsable = Column(String(150))
    correo_responsable = Column(String(150))
    telefono = Column(String(100))
    fecha_actualizacion = Column(Date)
