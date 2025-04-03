from flask import Flask
from .extensions import db, ma, migrate  # Import migrate from extensions
from .config import Config
from .tasks import tasks_bp
from .auth import auth_bp  # Import the auth blueprint
from flask_jwt_extended import JWTManager  # Import JWTManager

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Load configuration from the Config object
    app.config.from_object(Config)

    # Initialize the database, Marshmallow, and Flask-Migrate
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate with the app and db

    # Initialize JWTManager with the app
    jwt = JWTManager(app)  # Initialize JWTManager with the Flask app

    # Register the blueprints
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')  # Register the tasks blueprint
    app.register_blueprint(auth_bp, url_prefix='/api/auth')  # Register the auth blueprint

    return app