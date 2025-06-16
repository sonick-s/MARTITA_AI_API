from sqlalchemy.orm import Session
from models.interaccion import Interaccion

def get_interacciones(db: Session):
    return db.query(Interaccion).all()

def get_interaccion(db: Session, id_: int):
    return db.query(Interaccion).filter(Interaccion.id_interaccion == id_).first()

def create_interaccion(db: Session, data):
    nueva = Interaccion(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update_interaccion(db: Session, id_: int, data):
    interaccion = get_interaccion(db, id_)
    if not interaccion:
        return None
    for key, value in data.dict().items():
        setattr(interaccion, key, value)
    db.commit()
    db.refresh(interaccion)
    return interaccion

def delete_interaccion(db: Session, id_: int):
    interaccion = get_interaccion(db, id_)
    if not interaccion:
        return None
    db.delete(interaccion)
    db.commit()
    return interaccion
