# Generated by Django 4.2.11 on 2024-03-16 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_sheddetails_alter_instrumentmodel_instrument_range_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToolMovement",
            fields=[
                ("movement_id", models.AutoField(primary_key=True, serialize=False)),
                ("movement_date", models.DateField()),
                ("acknowledgment", models.BooleanField(default=False)),
                ("tool_count", models.IntegerField()),
                (
                    "destination_shed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="destination_shed",
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "instrument_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app1.instrumentmodel",
                    ),
                ),
                (
                    "source_shed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="source_shed",
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app1.instrumentgroupmaster",
                    ),
                ),
            ],
        ),
    ]
