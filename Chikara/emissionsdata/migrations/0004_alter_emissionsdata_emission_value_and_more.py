# Generated by Django 4.2.4 on 2023-09-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissionsdata', '0003_alter_emissionsdata_emission_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissionsdata',
            name='emission_value',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='vehicleemissions',
            name='emission_value',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
