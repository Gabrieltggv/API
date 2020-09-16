from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estabelecimento = db.Column(db.String(255), nullable=False)
    cliente = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
