from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {"form": form})

    subscription = form.save()

    _send_email('Confirmação de Inscrição',
                settings.DEFAULT_FROM_EMAIL,
                subscription.email,
                'subscriptions/subscription_email.txt',
                {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


detail = DetailView.as_view(model=Subscription)


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject,
                   body,
                   from_,
                   [from_, to])
