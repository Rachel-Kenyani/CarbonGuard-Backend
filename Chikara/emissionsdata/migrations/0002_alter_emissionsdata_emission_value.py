# Generated by Django 4.2.4 on 2023-09-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissionsdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissionsdata',
            name='emission_value',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
