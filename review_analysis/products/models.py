# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Products(models.Model):
	asin = models.TextField(max_length=10)
	reviews_url = models.TextField()
	product_title = models.TextField()
	date_created = models.DateTimeField(auto_now=True)