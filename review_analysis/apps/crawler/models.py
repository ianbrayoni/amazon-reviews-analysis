# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from review_analysis.apps.classifier.models import Sentiment, ColorCode


# Create your models here.

class Review(models.Model):
    asin = models.TextField()
    review_text = models.TextField()
    sentiment = models.ForeignKey(Sentiment)
    color = models.ForeignKey(ColorCode)
    date_created = models.DateTimeField(auto_now=True)
