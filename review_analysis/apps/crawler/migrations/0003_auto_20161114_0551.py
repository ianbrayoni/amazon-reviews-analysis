# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_reviews_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='sentiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Sentiment'),
        ),
    ]