# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('row_number', models.IntegerField(default=0)),
                ('glyphicon', models.CharField(max_length=30, default='asterisk')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=21)),
                ('row_number', models.IntegerField(default=0)),
                ('column_number', models.IntegerField(default=0)),
                ('progress_bar_color', models.CharField(max_length=6, default='335544')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('glyphicon', models.CharField(max_length=30)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValidationQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='category',
            field=models.ForeignKey(to='app.Category'),
            preserve_default=True,
        ),
    ]
