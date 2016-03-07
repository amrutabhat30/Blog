# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='down_vote',
            field=models.IntegerField(default=0, verbose_name=b'down Vote'),
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='up_vote',
            field=models.IntegerField(default=0, verbose_name=b'up Vote'),
        ),
    ]
