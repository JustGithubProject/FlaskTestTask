import os

from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv



# Parsing and loading .env file
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

