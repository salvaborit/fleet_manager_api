# Generated by Django 4.1.6 on 2023-02-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_valud_thru_documentation_valid_thru'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDocumentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('valid_thru', models.DateField()),
                ('renovation_alert', models.DateTimeField()),
                ('status', models.CharField(choices=[('VAL', 'Valido'), ('EXP', 'Expirado')], default='VAL', max_length=3)),
            ],
        ),
        migrations.RenameModel(
            old_name='Documentation',
            new_name='DriverDocumentation',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='documentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.vehicledocumentation'),
        ),
    ]