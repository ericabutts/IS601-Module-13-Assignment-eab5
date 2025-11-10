from sqlalchemy.orm import Session
from app import models
import hashlib

# Password hashing
def hash_password(password: str):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def verify_password(password: str, hashed: str):
    return hash_password(password) == hashed

# Create user
def create_user(db: Session, username: str, email: str, password: str):
    user = models.User(
        username=username,
        email=email,
        password_hash=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Authenticate
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None
