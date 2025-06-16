from sqlalchemy.orm import Session
from models.tramite import Tramite

def get_tramites(db: Session):
    return db.query(Tramite).all()

def get_tramite(db: Session, id_: int):
    return db.query(Tramite).filter(Tramite.id_tramite == id_).first()

def create_tramite(db: Session, tramite_data):
    nuevo = Tramite(**tramite_data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_tramite(db: Session, id_: int, tramite_data):
    tramite = get_tramite(db, id_)
    if not tramite:
        return None
    for key, value in tramite_data.dict().items():
        setattr(tramite, key, value)
    db.commit()
    db.refresh(tramite)
    return tramite

def delete_tramite(db: Session, id_: int):
    tramite = get_tramite(db, id_)
    if not tramite:
        return None
    db.delete(tramite)
    db.commit()
    return tramite
