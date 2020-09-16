from flask import Blueprint, request, make_response, current_app, jsonify

from app.serealizer import TransacaoSchema

bp_transacao = Blueprint('transacao', __name__)


@bp_transacao.route("/api/v1/transacao", methods=["POST"])
def mostrar():
    body = TransacaoSchema()
    trans= body.load(request.json)
    current_app.db.session.add(trans)
    current_app.db.session.commit()
    return make_response({
        "aceito": True
    }), 201
