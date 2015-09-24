# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 9, 19, 2, 18, 3, 561091, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
