# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-11 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0021_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDeploymentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('celery_id', models.TextField(blank=True, help_text='Celery task id for any background jobs running on this deployment', max_length=64, null=True, unique=True)),
                ('action', models.CharField(blank=True, max_length=255, null=True)),
                ('result', models.TextField(blank=True, help_text='Result of Celery task', max_length=16384, null=True)),
                ('status', models.CharField(blank=True, max_length=64, null=True)),
                ('traceback', models.TextField(blank=True, help_text='Celery task traceback, if any', max_length=16384, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='applicationdeployment',
            name='celery_task_id',
        ),
        migrations.RemoveField(
            model_name='applicationdeployment',
            name='task_result',
        ),
        migrations.RemoveField(
            model_name='applicationdeployment',
            name='task_status',
        ),
        migrations.RemoveField(
            model_name='applicationdeployment',
            name='task_traceback',
        ),
        migrations.AlterField(
            model_name='azure',
            name='region_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='azure',
            name='resource_group',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='azure',
            name='storage_account',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='azure',
            name='vm_default_user_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='azurecredentials',
            name='client_id',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='azurecredentials',
            name='secret',
            field=fernet_fields.fields.EncryptedCharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationdeploymenttask',
            name='deployment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baselaunch.ApplicationDeployment'),
        ),
    ]
