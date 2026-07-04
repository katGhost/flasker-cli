from sqlalchemy import SQLAlchemy
from bcrypt import Bcrypt

"""Extensions initialization
"""
bcrypt = Bcrypt()
db = SQLAlchemy()