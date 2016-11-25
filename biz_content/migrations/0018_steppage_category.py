# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-25 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biz_content', '0017_steppage_link_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='steppage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='step_pages', to='biz_content.Category'),
        ),
    ]
