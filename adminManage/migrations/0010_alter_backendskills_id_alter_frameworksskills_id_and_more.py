# Generated by Django 4.2 on 2023-04-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminManage', '0009_alter_backendskills_id_alter_frameworksskills_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backendskills',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='frameworksskills',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='frontendskills',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]