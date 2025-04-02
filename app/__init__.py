from flask import Flask
from .extensions import db, ma
from .config import Config
from .tasks import tasks_bp
from .auth import auth_bp  # Import the auth blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database and Marshmallow
    db.init_app(app)
    ma.init_app(app)

    # Register the tasks blueprint
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

    # Register the auth blueprint (with the '/api/auth' prefix)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')  # This will make '/register' accessible at '/api/auth/register'

    return app