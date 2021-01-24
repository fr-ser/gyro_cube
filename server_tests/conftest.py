from pathlib import Path

from httpx import AsyncClient
import pytest
from pytest_factoryboy import register
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from models.database import get_db

from .factories import GyroSideFactory

register(GyroSideFactory)

TEST_DB_FILE = Path("local_test.db")


@pytest.fixture
def auth():
    return ("me", "self")


@pytest.fixture
def db_session():
    TEST_DB_FILE.unlink(missing_ok=True)
    TEST_DB_FILE.touch()
    engine = create_engine(f"sqlite:///{TEST_DB_FILE.absolute()}",
                           connect_args={"check_same_thread": False})
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

    for mig in Path("migrations").glob("*.sql"):
        session.execute(mig.read_text())
    session.commit()

    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    return session


@pytest.fixture
async def client(auth):
    """
    API Client for integration tests
    """
    async with AsyncClient(app=app, base_url="http://test", auth=auth) as ac:
        yield ac
