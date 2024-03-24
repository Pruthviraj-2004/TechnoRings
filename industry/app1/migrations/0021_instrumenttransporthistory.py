# Generated by Django 4.2.11 on 2024-03-24 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0020_calibrationreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstrumentTransportHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "instrument",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.instrumentmodel",
                    ),
                ),
                (
                    "movement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.transportorder",
                    ),
                ),
            ],
        ),
    ]
