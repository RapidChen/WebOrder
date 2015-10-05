# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='ship',
            field=models.ForeignKey(verbose_name='运输方式', to='OrderSystem.Ship'),
        ),
    ]
