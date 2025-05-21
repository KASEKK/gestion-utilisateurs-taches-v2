# app/main.py

from sqlalchemy import create_engine
from app.config import URL_DB
from app.models import Base

def init_db():
    engine = create_engine(URL_DB)
    Base.metadata.create_all(engine)
    print("✅ Base de données et tables créées avec succès.")

if __name__ == "__main__":
    init_db()
 