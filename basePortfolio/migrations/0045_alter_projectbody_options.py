# Generated by Django 4.2 on 2023-04-27 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basePortfolio', '0044_delete_backendskills_delete_frameworks_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectbody',
            options={'ordering': ('-created',)},
        ),
    ]
