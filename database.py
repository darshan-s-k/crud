from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Format: postgresql://username:password@localhost:5432/database_name
# Update 'postgres' and 'password' with your local PostgreSQL credentials
DATABASE_URL = "postgresql://postgres:darshan%401360@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency injection provider for DB sessions per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()