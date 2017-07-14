# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 17:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0002_auto_20170714_1857'),
        ('challenges', '0002_auto_20170714_1855'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
                ('solved_challenge', models.ManyToManyField(blank=True, to='challenges.Challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
