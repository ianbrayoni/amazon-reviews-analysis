from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sentiment(models.Model):
    sentiment = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.sentiment


class LabeledData(models.Model):
    asin = models.TextField()
    review_text = models.TextField()
    sentiment = models.ForeignKey(Sentiment)

    def __str__(self):  # __unicode__ on Python 2
        return self.asin

