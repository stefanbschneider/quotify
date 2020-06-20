from django.db import models
from django.urls import reverse


class Quote(models.Model):
    quote_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.quote_text

    def get_absolute_url(self):
        """
        Absolute URL of a quote detail. Used for generic create/update views & model forms
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#model-forms
        """
        return reverse('detail', kwargs={'pk': self.pk})
