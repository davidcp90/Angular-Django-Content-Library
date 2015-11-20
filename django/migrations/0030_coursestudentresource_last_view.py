# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestudentresource',
            name='last_view',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 11, 13, 2, 775277), verbose_name='Ultima vez visto'),
            preserve_default=False,
        ),
    ]
