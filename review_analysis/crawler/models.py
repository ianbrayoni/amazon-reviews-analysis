from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Reviews(models.Model):
	asin = models.TextField()
	review_text = models.TextField()
	date_created = models.DateTimeField(auto_now=True)
