# Generated by Django 4.2.13 on 2024-06-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0050_servicetools_service_pending_tool"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="instrumentfamilygroup",
            unique_together={("instrument_family_name", "instrument_group_master")},
        ),
        migrations.AlterUniqueTogether(
            name="instrumentgroupmaster",
            unique_together={("tool_group_name", "tool_group_code")},
        ),
    ]
