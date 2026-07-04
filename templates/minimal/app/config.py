import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-super-secret-key")
    
    # SQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CORS
    CORS_ORIGIN = os.getenv("CORS_ORIGIN", "*")

    # DEBUG
    DEBUG = os.getenv("FLASK_DEBUG")
    