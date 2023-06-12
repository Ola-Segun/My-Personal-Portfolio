# Generated by Django 4.2 on 2023-04-21 21:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
