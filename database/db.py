import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///trading_bot.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    """
    Creates all database tables defined in models.py, if they don't
    already exist. Should be called once when the application starts.
    """
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully.")


def get_session():
    """
    Returns a new database session. Each session should be closed
    after use (typically with a try/finally block or context manager).
    """
    return SessionLocal()