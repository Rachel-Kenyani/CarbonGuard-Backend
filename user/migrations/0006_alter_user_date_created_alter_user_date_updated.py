# Generated by Django 4.2.5 on 2023-09-25 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_user_date_created_alter_user_date_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_created",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 25, 19, 34, 14, 358962, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_updated",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 25, 19, 34, 14, 358982, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]
