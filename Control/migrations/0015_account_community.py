# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Control', '0014_auto_20170524_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Control.Community')),
            ],
        ),
    ]
