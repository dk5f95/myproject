# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20171125_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product',
            new_name='product_name',
        ),
    ]