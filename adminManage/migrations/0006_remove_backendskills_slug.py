# Generated by Django 4.2 on 2023-04-27 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminManage', '0005_backendskills_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backendskills',
            name='slug',
        ),
    ]