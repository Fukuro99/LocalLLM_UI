from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./dev.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db() -> None:
    """Create database tables if they do not already exist."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """FastAPI dependency that yields a database session."""
    with Session(engine) as session:
        yield session
