# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyShellModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('mark', models.CharField(blank=True, default='\u65e0\u8bf4\u660e', max_length=50)),
                ('ip', models.CharField(max_length=30)),
                ('script', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('UserPass', models.CharField(max_length=50)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='myshellmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webknife.UserModels'),
        ),
    ]