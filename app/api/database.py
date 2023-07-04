from sqlmodel import Session, create_engine

# TODO: Implement settings module
from app.core.settings import get_settings

settings = get_settings()


def get_session():
    engine = create_engine(settings.POSTGRES_DSN)
    with Session(engine) as session:
        yield session
