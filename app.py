from flask import Flask
from flask_cors import CORS 
from config.db import db, get_database_uri
from routes.task_routes import task_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(task_routes, url_prefix='/tasks')

    @app.route('/ping')
    def ping():
        return 'pong'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)