from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField

from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput, label='telefone')

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
