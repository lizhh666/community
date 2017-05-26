# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0012_auto_20170524_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='community',
        ),
        migrations.AddField(
            model_name='activity',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_activity', to='Control.Community'),
        ),
    ]
