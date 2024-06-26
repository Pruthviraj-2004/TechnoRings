# Generated by Django 4.2.13 on 2024-06-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0056_alter_instrumentgroupmaster_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instrumentfamilygroup",
            name="instrument_group_master",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app1.instrumentgroupmaster",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="instrumentgroupmaster",
            unique_together={("tool_group_name", "tool_group_code")},
        ),
    ]
