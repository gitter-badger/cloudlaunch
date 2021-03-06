# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-12 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0022_auto_20170811_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('FEATURED', 'Featured'), ('GALAXY', 'Galaxy'), ('SCALABLE', 'Scalable'), ('VM', 'Virtual machine')], max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'App categories',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('DEV', 'Development'), ('CERTIFICATION', 'Certification'), ('LIVE', 'Live')], default='DEV', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applicationdeploymenttask',
            name='action',
            field=models.CharField(blank=True, choices=[('LAUNCH', 'Launch'), ('HEALTH_CHECK', 'Health check'), ('DELETE', 'Delete')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicationdeploymenttask',
            name='deployment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='baselaunch.ApplicationDeployment'),
        ),
        migrations.AddField(
            model_name='application',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='baselaunch.AppCategory'),
        ),
    ]
