# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]