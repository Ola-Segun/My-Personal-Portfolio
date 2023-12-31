# Generated by Django 4.2 on 2023-04-17 10:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('basePortfolio', '0030_alter_projectbody_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='projectbody',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
