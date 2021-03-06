from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Julio Saraiva',
            slug='julio-saraiva',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='julinux@saraiva.com.br'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='61-98230-3695'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL,
                          value='julinux@saraiva.com.br')
        self.assertEqual('julinux@saraiva.com.br', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name="Alan Turing",
            slug="alan-turing",
            photo="http://hbn.link/turing-pic"
        )

        s.contact_set.create(kind=Contact.EMAIL, value="alan@turing.com")
        s.contact_set.create(kind=Contact.PHONE, value="61-21219021")

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['alan@turing.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['61-21219021']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
