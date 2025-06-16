from sqlalchemy.orm import Session
from models.usuario import Usuario
from passlib.hash import bcrypt

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, id_: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_).first()

def create_usuario(db: Session, usuario_data):
    hashed_password = bcrypt.hash(usuario_data.password)
    usuario_dict = usuario_data.dict()
    usuario_dict['password'] = hashed_password
    nuevo = Usuario(**usuario_dict)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_usuario(db: Session, id_: int, usuario_data):
    usuario = get_usuario(db, id_)
    if not usuario:
        return None
    for key, value in usuario_data.dict().items():
        if key == 'password':
            value = bcrypt.hash(value)
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

def delete_usuario(db: Session, id_: int):
    usuario = get_usuario(db, id_)
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return usuario
