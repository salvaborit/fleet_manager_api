# Generated by Django 4.1.6 on 2023-02-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='valud_thru',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dob',
            field=models.DateField(),
        ),
    ]