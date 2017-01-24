# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-16 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0002_auto_20161021_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='ethnicity',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Ethnicity'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='gender',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Gender'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='identity',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Identity'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='sexual_orientation',
            field=models.ManyToManyField(blank=True, to='mentalhealth.SexualOrientation'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Tag'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='therapist_recommendation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='therapist_strategy',
            field=models.TextField(blank=True, null=True),
        ),
    ]
