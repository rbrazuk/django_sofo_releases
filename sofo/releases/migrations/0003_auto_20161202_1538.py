# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-02 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_release_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='cover',
            field=models.ImageField(default='releases/cover_images/no_img.jpg', upload_to='releases/cover_images'),
        ),
    ]
