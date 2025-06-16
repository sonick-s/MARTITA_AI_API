from sqlalchemy.orm import Session
from models.direccion import Direccion

def get_direcciones(db: Session):
    return db.query(Direccion).all()

def get_direccion(db: Session, id_: int):
    return db.query(Direccion).filter(Direccion.id_direcciones == id_).first()

def create_direccion(db: Session, direccion_data):
    nueva = Direccion(**direccion_data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update_direccion(db: Session, id_: int, direccion_data):
    direccion = get_direccion(db, id_)
    if not direccion:
        return None
    for key, value in direccion_data.dict().items():
        setattr(direccion, key, value)
    db.commit()
    db.refresh(direccion)
    return direccion

def delete_direccion(db: Session, id_: int):
    direccion = get_direccion(db, id_)
    if not direccion:
        return None
    db.delete(direccion)
    db.commit()
    return direccion
