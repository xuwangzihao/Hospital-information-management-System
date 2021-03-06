# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=30, unique=True, verbose_name='\u8d26\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.CharField(max_length=30, unique=True, verbose_name='\u6570\u636e\u5e93\u540d')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('info', models.TextField(verbose_name='\u7b80\u4ecb')),
            ],
        ),
        migrations.CreateModel(
            name='Myadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=30, unique=True, verbose_name='\u8d26\u53f7')),
                ('password', models.CharField(max_length=30, verbose_name='\u5bc6\u7801')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yfzz.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=30, unique=True, verbose_name='\u8d26\u53f7')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yfzz.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yfzz.Hospital'),
        ),
    ]
