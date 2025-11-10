# from main import app
# from app.database import get_db
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.models import Base
# import pytest
# from fastapi.testclient import TestClient

# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
# engine = create_engine(DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# @pytest.fixture
# def client():
#     return TestClient(app)
