from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sentiment(models.Model):
    sentiment = models.TextField()

    def __unicode__(self):
        return str(self.sentiment)


class ColorCode(models.Model):
    color = models.TextField()

    def __unicode__(self):
        return str(self.color)


class TrainData(models.Model):
    asin = models.TextField()
    review_text = models.TextField()
    sentiment = models.ForeignKey(Sentiment)

    def __unicode__(self):
        return str(self.asin)

