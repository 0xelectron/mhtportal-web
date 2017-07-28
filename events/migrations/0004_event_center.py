# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20170719_0915'),
        ('events', '0003_auto_20170715_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='center',
            field=models.ForeignKey(default=None, help_text='Center', on_delete=django.db.models.deletion.CASCADE, related_name='center', to='base.Center'),
            preserve_default=False,
        ),
    ]
