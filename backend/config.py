import os

from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv


load_dotenv()


# Database variables
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Swagger variables
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Test-Task-Python-Flask'
    }
)


# Flask-app variables
FLASH_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True
