# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_report_verified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='projects.Task'),
        ),
    ]