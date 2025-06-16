from sqlalchemy.orm import Session
from models.prompt_bot import PromptBot

def get_prompts(db: Session):
    return db.query(PromptBot).all()

def get_prompt(db: Session, id_: int):
    return db.query(PromptBot).filter(PromptBot.id_prompt == id_).first()

def create_prompt(db: Session, data):
    nuevo = PromptBot(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_prompt(db: Session, id_: int, data):
    prompt = get_prompt(db, id_)
    if not prompt:
        return None
    for key, value in data.dict().items():
        setattr(prompt, key, value)
    db.commit()
    db.refresh(prompt)
    return prompt

def delete_prompt(db: Session, id_: int):
    prompt = get_prompt(db, id_)
    if not prompt:
        return None
    db.delete(prompt)
    db.commit()
    return prompt
