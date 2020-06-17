import json
import random

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Quote


class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    # instead of the default "object_list"
    context_object_name = 'quote_list'

    def get_queryset(self):
        """Return all quotes"""
        return Quote.objects.all().order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Quote
    template_name = 'quotes/detail.html'


def rand_quote(request):
    """View a random quote"""
    rand_quote = random.choice(Quote.objects.all())
    context = {'quote': rand_quote}
    return render(request, 'quotes/random.html', context)


