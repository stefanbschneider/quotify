import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Quote


def create_quote(quote_text, pub_date=timezone.now(), likes=0):
    """Create a quote with a given number of likes"""
    return Quote.objects.create(quote_text=quote_text, pub_date=pub_date, likes=likes)


class QuoteIndexViewTests(TestCase):
    def test_no_quotes(self):
        """If now quotes exist, an appropriate message is displayed."""
        response = self.client.get(reverse('quotes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No quotes available.")
        self.assertQuerysetEqual(response.context['quote_list'], [])

    def test_one_quote(self):
        """Create one quote and test if it's listed"""
        create_quote(quote_text='Quote one')
        response = self.client.get(reverse('quotes:index'))
        self.assertQuerysetEqual(response.context['quote_list'], ['<Quote: Quote one>'])

    def test_two_quotes(self):
        """Create two quotes and test if they are listed in the right order (newest first)"""
        create_quote(quote_text='Quote one')
        create_quote(quote_text='Quote two')
        response = self.client.get(reverse('quotes:index'))
        self.assertQuerysetEqual(response.context['quote_list'], ['<Quote: Quote two>', '<Quote: Quote one>'])
