from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class PromptBot(Base):
    __tablename__ = 'prompts_bot'
    
    id_prompt = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(String(50))
    contenido = Column(Text, nullable=False)
    prioridad = Column(Integer, default=0)
    fecha_creacion = Column(DateTime)
