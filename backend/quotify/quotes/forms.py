from django import forms

from .models import Quote


# class QuoteForm(forms.Form):
#     quote_text = forms.CharField()

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quote_text',)
