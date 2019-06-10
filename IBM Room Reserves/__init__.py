from slask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app= Flask(__name__)


    app.config ['SQLALCHEMY_DATABASE_URI
    '] = 'sqlite:///api_demo.bd'

    from .views import main
    app.register-blueprint(main)
    

    return app