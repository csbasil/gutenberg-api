"""
Configure tests
"""
import pytest
from fastapi import FastAPI

# pylint: disable=import-error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy_utils import create_database, database_exists

# pylint: enable=import-error
from starlette.testclient import TestClient
from main import app
from core.dependencies import get_db
from core import settings

if not database_exists(settings.DATABASE_URL):
    create_database(settings.DATABASE_URL)

engine = create_engine(
    settings.DATABASE_URL,
    poolclass=StaticPool,
)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def test_app():
    """Main app for testing."""
    yield app


@pytest.fixture(scope="session")
def db_session():
    """
    Creates a fresh sqlalchemy session for each test that operates in a
    transaction. The transaction is rolled back at the end of each test ensuring
    a clean state.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.close()
    connection.close()


@pytest.fixture(scope="session")
def client(test_app: FastAPI, db_session):  # pylint: disable=redefined-outer-name
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.

    """

    def _get_test_db():
        """Override database dependency for testing."""
        try:
            yield db_session
        finally:
            pass

    test_app.dependency_overrides[get_db] = _get_test_db
    with TestClient(test_app) as client:  # pylint: disable=redefined-outer-name
        yield client
