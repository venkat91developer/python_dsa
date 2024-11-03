from .user_model import User  # Change this to user_model
from .db import db  # Keep this if you have a db instance

__all__ = ['User', 'db']
