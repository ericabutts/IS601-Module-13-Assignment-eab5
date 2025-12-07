# app/crud.py
from sqlalchemy.orm import Session
from . import models, security
from datetime import datetime

# -----------------------
# User CRUD operations
# -----------------------

def create_user(db: Session, user_in):
    """
    Create a new user in the database.
    """
    try:
        user = models.User(
            username=user_in.username,
            email=user_in.email,
            password_hash=security.hash_password(user_in.password),
            created_at=datetime.now()
        )
        db.add(user)
        db.commit()      # commit to persist the user
        db.refresh(user) # refresh to get the auto-generated ID
        return user
    except:
        db.rollback()
        raise

def authenticate_user(db: Session, username: str, password: str):
    """
    Authenticate user by username and password.
    """
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and security.verify_password(password, user.password_hash):
        return user
    return None
