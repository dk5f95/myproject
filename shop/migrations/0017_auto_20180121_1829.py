# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 18:29
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20180120_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='closingDay',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('Not any day', 'None')], default='Not any day', max_length=68),
        ),
    ]