# Generated by Django 4.2 on 2023-04-17 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('basePortfolio', '0029_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectbody',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
