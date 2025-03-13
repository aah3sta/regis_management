from flask import Flask
from .routes import routes
from .config import settings
from .database import Student, get_db
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.secret_key = settings.SECRET_KEY
    app.register_blueprint(routes, url_prefix='/')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'

    @login_manager.user_loader
    def load_user(student_id):
        db = get_db()
        return db.query(Student).get(int(student_id))

    return app