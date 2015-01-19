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
            name='Map',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('map_title', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pin_latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('pin_longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('category', models.CharField(choices=[('SL', 'Sleep'), ('EA', 'Eat'), ('OU', 'Outdoor Activity'), ('CU', 'Culture'), ('SH', 'Shopping'), ('NL', 'Nightlife'), ('CO', 'Contact'), ('OT', 'Other')], max_length=2)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
