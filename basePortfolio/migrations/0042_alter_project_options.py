# Generated by Django 4.2 on 2023-04-20 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basePortfolio', '0041_alter_project_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('created',)},
        ),
    ]