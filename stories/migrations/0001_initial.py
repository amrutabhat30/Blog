# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'title')),
                ('link', models.TextField(max_length=200, verbose_name=b'link')),
                ('up_vote', models.IntegerField(verbose_name=b'up Vote')),
                ('down_vote', models.IntegerField(verbose_name=b'down Vote')),
                ('flag', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField()),
                ('modified_on', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
            bases=(models.Model,),
        ),
    ]
