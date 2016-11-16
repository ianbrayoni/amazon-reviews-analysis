# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
# from review_analysis.apps.classifier.models import Sentiment


# Create your models here.

class Reviews(models.Model):
    asin = models.TextField()
    review_text = models.TextField()
    sentiment = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
