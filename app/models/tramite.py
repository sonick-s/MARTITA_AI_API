from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tramite(Base):
    __tablename__ = 'tramites'
    
    id_tramite = Column(Integer, primary_key=True)
    id_unidad = Column(Integer, ForeignKey('direcciones.id_direcciones'))
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    contexto = Column(Text)
    requisitos = Column(Text)
    pasos = Column(Text)
    links_formularios = Column(Text)
    fecha_registro = Column(DateTime)

    direccion = relationship('Direccion')
