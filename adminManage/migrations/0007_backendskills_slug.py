# Generated by Django 4.2 on 2023-04-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminManage', '0006_remove_backendskills_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='backendskills',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
