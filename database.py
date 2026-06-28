import os  # <-- Step 1: Import the built-in operating system module
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Step 2: Use os.getenv to check for the cloud environment variable.
# If it doesn't exist (like on your laptop), it falls back to your local string.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:darshan%401360@localhost:5432/fastapi_db"
)

# Step 3: Handle a common legacy driver prefix quirk found in some cloud platforms
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
