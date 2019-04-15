# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-03 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        # migrations.CreateModel(
        #     name='Sender',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('messengerSenderID', models.TextField()),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='memory',
        #     name='sender',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Sender'),
        # ),
        # migrations.AddField(
        #     model_name='conversation',
        #     name='sender',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Sender'),
        # ),
    ]
