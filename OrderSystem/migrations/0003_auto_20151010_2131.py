# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderSystem', '0002_auto_20151005_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(verbose_name='图片', upload_to='./common_static/pic'),
        ),
    ]
