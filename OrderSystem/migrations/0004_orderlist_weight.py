# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderSystem', '0003_auto_20151010_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='weight',
            field=models.IntegerField(verbose_name='总重', default=20),
            preserve_default=False,
        ),
    ]
