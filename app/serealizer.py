from flask_marshmallow import Marshmallow
from app.model import Transacao


mar = Marshmallow()


def configure(app):
    mar.init_app(app)


class TransacaoSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = Transacao
        include_relationships = True
        load_instance = True
