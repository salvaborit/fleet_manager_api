# Generated by Django 4.1.6 on 2023-02-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
