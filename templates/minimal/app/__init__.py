from flask import Flask
from app.extensions import db


def create_app():
    app = Flask(__name__)

    # Config FIRST
    app.config.from_object('app.config.Config')
    app.secret_key = app.config['SECRET_KEY']

    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints below
    from app.routes import app_bp   # NOTE: blueprints imports can also be defined at the top
    app.register_blueprint(app_bp)

    # create tables if they do not exist
    with app.app_context():
        db.create_all()


    return app


