# Generated by Django 4.2.11 on 2024-03-21 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0018_remove_vendorsent_tool_remove_vendorsent_vendor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryChallan",
            fields=[
                (
                    "deliverychallan_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("received_date", models.DateField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app1.serviceorder",
                    ),
                ),
                (
                    "shed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="shed_delivery_challan",
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app1.vendor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryChallanTools",
            fields=[
                (
                    "deliverychallantool_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "deliverychallan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app1.deliverychallan",
                    ),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app1.instrumentmodel",
                    ),
                ),
            ],
        ),
    ]