# Generated by Django 4.2 on 2023-04-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basePortfolio', '0020_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
