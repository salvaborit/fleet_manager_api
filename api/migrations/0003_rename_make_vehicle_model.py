# Generated by Django 4.1.6 on 2023-02-07 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='make',
            new_name='model',
        ),
    ]
