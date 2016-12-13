from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField

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


class Analysed(models.Model):
    asin = models.TextField()
    title = models.TextField()
    sentiment_distribution = ArrayField(HStoreField())
    total_reviews = models.IntegerField()

    def __unicode__(self):
        return str(self.asin)


