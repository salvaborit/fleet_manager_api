# Generated by Django 4.1.6 on 2023-02-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_driverdocumentation_renovation_alert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledocumentation',
            name='renovation_alert',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]