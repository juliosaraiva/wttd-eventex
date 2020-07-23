from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Julio Saraiva', cpf='12345678911',
                    email="test@email.com", phone="61-99162-8287")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'contato@juliosaraiva.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            "Julio Saraiva",
            "12345678911",
            "test@email.com",
            "61-99162-8287"
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
