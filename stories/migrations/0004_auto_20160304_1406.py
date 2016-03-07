# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20160303_0530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=250, verbose_name=b'text')),
                ('posted_on', models.DateTimeField(auto_now_add=True, verbose_name=b'posted On')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name=b'modified On')),
                ('story', models.ForeignKey(to='stories.Story')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='story',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'created On'),
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name=b'modified On'),
        ),
    ]
