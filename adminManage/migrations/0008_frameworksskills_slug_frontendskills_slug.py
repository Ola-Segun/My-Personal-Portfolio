# Generated by Django 4.2 on 2023-04-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminManage', '0007_backendskills_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='frameworksskills',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frontendskills',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
