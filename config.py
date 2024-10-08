from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{DATABASE_PASSWORD}@localhost/rest_api'
    DEBUG = True