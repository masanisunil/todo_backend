from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS


db=SQLAlchemy()
migrate=Migrate()


def create_app():
    app=Flask(__name__)

    CORS(app)

    app.config.from_object(Config)


    db.init_app(app)

    migrate.init_app(app,db)

    from app.routes import todo_bp
    app.register_blueprint(todo_bp)

    return app