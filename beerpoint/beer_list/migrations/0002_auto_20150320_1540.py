# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beertable',
            name='beer_calory',
            field=models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xb0\xd0\xbb\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beertable',
            name='beer_date_public',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beertable',
            name='beer_maker',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2'),
            preserve_default=True,
        ),
    ]
