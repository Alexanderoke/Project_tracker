# Generated by Django 3.0 on 2022-04-03 21:37

import django.contrib.postgres.fields
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220401_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_members',
        ),
        migrations.AddField(
            model_name='project',
            name='project_member',
            field=django.contrib.postgres.fields.ArrayField(base_field=jsonfield.fields.JSONField(default=dict), default=list, null=True, size=None),
        ),
    ]
