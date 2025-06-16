from sqlalchemy import Column, Integer, Text, DateTime
from database import Base

class Interaccion(Base):
    __tablename__ = 'interacciones'
    
    id_interaccion = Column(Integer, primary_key=True)
    pregunta = Column(Text)
    respuesta = Column(Text)
    respuesta_util = Column(Text, default=None)
    fecha = Column(DateTime)
