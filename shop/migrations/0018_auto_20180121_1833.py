# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 18:33
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20180121_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='closingDay',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('Not any day', 'None')], default='None', max_length=68),
        ),
    ]
