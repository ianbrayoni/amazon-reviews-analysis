from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Reviews(models.Model):
	review_text = models.TextField()
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.review_text