# Generated by Django 4.1.6 on 2023-02-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_vehicledocumentation_renovation_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverdocumentation',
            name='renovation_alert',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
