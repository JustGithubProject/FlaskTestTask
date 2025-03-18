""" File that represents entry point """
from flask import Flask

from routes import user_routes
from models import db
from config import (
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS
)


# Creating an application object and registering user routes
app = Flask(__name__)
app.register_blueprint(user_routes)


# Set up config variables
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)

# Creating tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
