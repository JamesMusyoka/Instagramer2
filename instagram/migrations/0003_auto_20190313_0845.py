# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20190313_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
