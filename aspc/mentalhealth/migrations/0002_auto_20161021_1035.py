# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-21 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='tags',
            field=models.ManyToManyField(to='mentalhealth.Tag'),
        ),
        migrations.AlterField(
            model_name='therapist',
            name='qualifications',
            field=models.ManyToManyField(to='mentalhealth.Qualification'),
        ),
    ]
