# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20160303_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='link',
            field=models.URLField(verbose_name=b'link'),
        ),
    ]
