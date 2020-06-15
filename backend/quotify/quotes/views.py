from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

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
