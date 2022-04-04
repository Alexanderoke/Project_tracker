# Generated by Django 3.0 on 2022-04-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220403_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_members',
        ),
        migrations.AddField(
            model_name='project',
            name='project_member',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(max_length=100),
        ),
    ]