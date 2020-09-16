from unittest import TestCase

from flask import url_for

from app.app import create_app


class IndexTest(TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()

    # import ipdb
    # ipdb.set_trace()

    def tearDown(self) -> None:
        # self.app.db.session.remove()
        # self.app.db.drop_all()
        self.app.db.session.close()

    def test_trasacao(self):
        dado = {
            'estabelecimento': '37.256.187/0001-56',
            'cliente': '094.214.930-01',
            'valor': 890,
            'descricao': 'Janta em restaurante chique pago via Shirpay!',
        }

        response = self.client.post(url_for('transacao.mostrar'), json=dado)
        self.assertEqual(response.status_code, 201)
        self.assertEqual({'aceito': True}, response.json)
