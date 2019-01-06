from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Julio Saraiva', cpf='91963230272',
                    email="contato@juliosaraiva.com.br", phone="61-99162-8287")
        self.resp = self.client.post(r('subscriptions:new'), data)
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
            "91963230272",
            "contato@juliosaraiva.com.br",
            "61-99162-8287"
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
