# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-17 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0015_add_application_version_unique_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdeployment',
            name='task_status',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='applicationdeployment',
            name='task_traceback',
            field=models.TextField(blank=True, help_text='Celery task traceback, if any', max_length=16384, null=True),
        ),
        migrations.AlterField(
            model_name='applicationdeployment',
            name='task_result',
            field=models.TextField(blank=True, help_text='Result of Celery task', max_length=16384, null=True),
        ),
    ]
