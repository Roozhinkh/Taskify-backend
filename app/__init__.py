from flask import Flask 
from .extensions import db, ma
from .config import Config 
from .tasks import tasks_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

    return app 

