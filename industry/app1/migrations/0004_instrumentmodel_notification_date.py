# Generated by Django 4.2.13 on 2024-06-23 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_alter_instrumentgroupmaster_tool_family"),
    ]

    operations = [
        migrations.AddField(
            model_name="instrumentmodel",
            name="notification_date",
            field=models.DateField(
                blank=True, default=datetime.datetime(2024, 6, 23, 0, 0), null=True
            ),
        ),
    ]
