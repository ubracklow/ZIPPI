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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pin_latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('pin_longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('category', models.CharField(max_length=2, choices=[('SL', 'Sleep'), ('EA', 'Eat'), ('OU', 'Outdoor Activity'), ('CU', 'Culture'), ('SH', 'Shopping'), ('NL', 'Nightlife'), ('CO', 'Contact'), ('OT', 'Other')])),
                ('comment', models.TextField()),
                ('map_id', models.ForeignKey(to='zippi.Map')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
