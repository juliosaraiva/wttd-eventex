from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Cliente Silva', cpf='12345678911',
                    email="cliente@gmail.com", phone="61-99162-8287")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'cliente@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            "Cliente Silva",
            "12345678911",
            "cliente@gmail.com",
            "61-99162-8287"
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
