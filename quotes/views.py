import os
import json
import random

from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.template import loader
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Quote


# functions
def send_email(msg):
    """Send email containing the message via sendgrid"""
    print(f"Trying to send email with msg: {msg}")
    # get destination address and API key from env vars
    dest_mail = os.getenv('EMAIL', None)
    api_key = os.environ.get('SENDGRID_API_KEY', None)
    if dest_mail is None or api_key is None:
        print("Env var 'EMAIL' or 'SENDGRID_API_KEY' missing. Can't send email.")
        return "Env var 'EMAIL' or 'SENDGRID_API_KEY' missing. Can't send email."

    email = Mail(from_email='hello@world.com', to_emails=dest_mail, subject='Quotify: Change Notification',
                 html_content=msg)
    try:
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(email)
        print(f"Email response status code: {response.status_code}")
        return f"Sent email with msg: {msg} to {dest_mail}. Status code: {response.status_code}"
    except Exception as e:
        print(e.message)

def like(request, quote_id):
    """Like a specific quote"""
    # TODO: I should do this in a responsive manner in JS or Vue without page reload
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.likes += 1
    quote.save()
    return HttpResponseRedirect(reverse('quotes:detail', args=(quote.id,)))


def rand_quote(request):
    """View a random quote"""
    rand_quote = random.choice(Quote.objects.all())
    # forward to detail view of randomly selected quote
    return HttpResponseRedirect(reverse('quotes:detail', args=(rand_quote.id,)))


# basic, gerenic views
class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    # instead of the default "object_list"
    context_object_name = 'quote_list'

    def get_queryset(self):
        """Return all quotes"""
        return Quote.objects.all().order_by('-pub_date')
        # TODO: trying to return json that I can then use with Vue.js; didn't work
        # wrap in list because QuerySet is not Json serializable
        # data = list(Quote.objects.values())
        # return JsonResponse(data, safe=False)


class DetailView(generic.DetailView):
    model = Quote
    template_name = 'quotes/detail.html'


# gerneric edit views
class QuoteCreate(CreateView):
    # default template for create & update: quotes/quote_form.html
    template_name = 'quotes/quote_form.html'
    model = Quote
    fields = ['quote_text']
    # object_change = send_email(f"New quote: {str(object)}")


class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['quote_text']
    # object_change = send_email(f"Updated quote: {str(object)}")


class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('quotes:index')
