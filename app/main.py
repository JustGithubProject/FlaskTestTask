""" File that represents entry point """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes import user_routes

from config import (
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS
)


# Creating an application object and registering user routes
app = Flask(__name__)
app.register_blueprint(user_routes)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
