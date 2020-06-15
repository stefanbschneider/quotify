from django.db import models


class Quote(models.Model):
    quote_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.quote_text
