# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0004_auto_20170828_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document1', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
