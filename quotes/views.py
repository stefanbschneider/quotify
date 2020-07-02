import json
import random

from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.template import loader

from .models import Quote


# functions
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


class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['quote_text']


class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('quotes:index')
