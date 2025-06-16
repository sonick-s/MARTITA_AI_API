from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import pymysql

# Configuración de conexión
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "martita_ia"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

ascii_art = r"""
                 __  __   _   ___ _____ ___ _____ _         ___   _   
                |  \/  | /_\ | _ \_   _|_ _|_   _/_\       |_ _| /_\ 
                | |\/| |/ _ \|   / | |  | |  | |/ _ \       | | / _ \ 
                |_|  |_/_/ \_\_|_\ |_| |___| |_/_/ \_\____ |___/_/ \_/
                                                      |___|         
                """
print(ascii_art)
print("Bienvenido a la API de Martita IA, creada como trabajo de grado -Jean De La Cruz , Omar Sani ")

# Crear motor de SQLAlchemy
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print(" ")
    print(" --------------------------------------------")
    print("✅ Conexión exitosa a la base de datos")
    print(" --------------------------------------------")
    print(" ")
    connection.close()
except Exception as e:
    print(" --------------------------------------------")
    print("❌ Error al conectar a la base de datos:")
    print(e)
    print(" --------------------------------------------")

# Crear sesión local y base declarativa
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener sesión de base de datos (para usar como dependencia en FastAPI)
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
