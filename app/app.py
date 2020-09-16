from flask import Flask
from flask_migrate import Migrate

from app.model import configure as config_db
from app.serealizer import configure as config_mar




def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gabriel:8611jo@localhost:3306/api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_mar(app)

    Migrate(app, app.db)

    from app.view import bp_transacao
    app.register_blueprint(bp_transacao)

    return app

