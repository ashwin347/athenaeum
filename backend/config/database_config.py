from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine
engine = create_engine('sqlite:///data_db.db', connect_args={"check_same_thread": False})
# Create a base class for declarative models
SessionLocal = sessionmaker(bind=engine)
try:
    engine.connect()
except Exception as e:
    print('unable to connect to db')
Base = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
