# Generated by Django 4.2 on 2023-06-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminManage', '0012_rename_profileimage_profileimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
